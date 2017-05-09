# TaintClassify
[SeCloud](http://www.securit-brussels.be/project/secloud/) project on classifying node.js sinks and sources. Based on OWASP list of JavaScript vulnerabilities. Inspired by the paper by Rasthofer et al. [A Machine-learning Approach for Classifying and Categorizing Android Sources and Sinks](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.432.7534&rep=rep1&type=pdf)

#### App for classifying can be found in the [secloudapp](secloudapp) folder.

# JSON data format
Data is extracted from the multiple files downloaded from node.js and located in [json](data/json) folder.

Currently only the 'textRaw' and 'params' are taken into account. Those are aggregated
in data.json.

Format is as follows:
```json
{
    "cl": 0,
    "params": [
        "value",
        "message"
    ],
    "textRaw": "assert(value[, message])"
}
```

Param ```"cl"``` refers to the class. There are three classes in this dataset:
```json
    neither:    0
    source:     1
    sink:       2
```    

For unknown class: 
```json
cl: -1
```

The python file that handles parsing is [processJSON.py](data/json/processJSON.py)

## Features

For handcrafted features to be used as input look at [helperJSON.py](data/helperJSON.py)

Currently features are binary(*is a feature present*) and extracted from method names. Features are based on OWASP list of JavaScript vulnerabilities e.g. ```get``` usually is a source of information. There are 15 such features extracted.

### Issues
- Dataset is small with 265 hand annotated examples.
- Hand crafted features do not cover all possible cases of a source or a sink in Node.js hence some valuable info for classification is missing.

