import sys
#sys.path.append('data')
import numpy as np
from data.helperJSON import DataProcess
from pprint import pprint
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import argparse
import os.path
from sklearn.externals import joblib
import os
dir = os.path.dirname(__file__)



# Add a function to check for path on arguments
def arg_exist(x):
    if not os.path.exists(x):
        raise argparse.ArgumentTypeError("{0} does not exist".format(x))
    return x

# Function to return text for class. 0: nothing, 1: source, 2: sink
def get_class(cl):
    if cl == 0:
        return 'Neither'
    if cl == 1:
        return 'Source'
    if cl == 2:
        return 'Sink'

# Add a parser for cmd arguments. Useful for calling later through Electron
parser = argparse.ArgumentParser()
parser.add_argument('-f', default = os.path.join(dir,'data/json/data.json'), type = arg_exist,  dest = 'filename')
parser.add_argument('-l', action = 'store_true', dest = 'learning')
args = parser.parse_args()

# If learning load the dataset along with the labels
if args.learning:
    dp = DataProcess(data_file = args.filename, learning = args.learning)
    X, y = (dp.X, dp.y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(X.shape, y.shape)

    # Set the parameters by cross-validation
    C_space = np.logspace(0, 5, 6)
    gamma_space = np.logspace(-6, -1, 6)
    tuned_parameters = [{'kernel': ['rbf'], 'gamma': gamma_space,
                         'C': C_space},
                        {'kernel': ['linear'], 'C': C_space}]

    print("# Tuning hyper-parameters")
    print()

    clf = GridSearchCV(SVC(), tuned_parameters, cv=5)
    clf.fit(X_train, y_train)

    print("Best parameters set found on train set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on train set:")
    print()
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full train set.")
    print("The scores are computed on the full test set.")
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))
    print()
    print("Saving model")
    model_file = os.path.join(dir, "svm_model.plk")
    joblib.dump(clf, model_file)

else: # Not learning but just doing prediction. Checking for sigle method or file
    print("Prediction on file {0}".format(args.filename))
    dp = DataProcess(data_file = args.filename, learning = args.learning)
    X, meth_txt = (dp.X, dp.meth_txt)
    #print(X.shape)
    model_file = os.path.join(dir, 'svm_model.plk')
    if os.path.exists(model_file):
        clf = joblib.load(model_file)
        predictions = [get_class(pr) for pr in clf.predict(X)]
        for met, cl in zip(meth_txt, predictions):
            print(met, cl)
    else:
        print("{} file does not exist".format(model_file))
