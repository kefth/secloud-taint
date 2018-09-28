import sys
#sys.path.append('data')
import numpy as np
from data.helperJSON import DataProcess
from pprint import pprint
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
        return ''
    if cl == 1:
        return 'Source'
    if cl == 2:
        return 'Sink'

# Add a parser for cmd arguments. Useful for calling later through Electron
parser = argparse.ArgumentParser()
parser.add_argument('-f', default = os.path.join(dir,'data/json/data.json'), type = arg_exist,  dest = 'filename')
args = parser.parse_args()

 # Not learning but just doing prediction. Checking for sigle method or file
print("Prediction on file {0}".format(args.filename))
dp = DataProcess(data_file = args.filename, learning = False)
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
