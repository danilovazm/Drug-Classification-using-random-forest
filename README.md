# Drug Classification using random forest

## About

The main goal of this project is to predict which drug would fit better for each patient.

### Dataset
For this project a [public dataset](https://www.kaggle.com/datasets/prathamtripathi/drug-classification) from Kaggle was used.

### Implementation
The code was implemented in python using pandas and scikit-learn libraries. Also, some preprocessing of the data was needed: categorical objects were transform into numerical objects. For the prediction the ensemble method, Random Forest, was used.

### Summary
`Main.py`: file that trains the model based on users choice and prints the model's result.

`PreProcess.py`: file where the dataset is preprocessed and splitted into train and test.

## How To
The python version used in this project was:
```
    Python 3.7.3
```

First you will need to install the following dependencies:
``` 
    pip install pandas
    pip install scikit-learn
```
Once the dependencies were installed to run the code go to the root of this repository and execute the command below:
``` 
    python Main.py
```
Also, when running the Main.py file, is possible to fit some methods' parameters. To do so choose at least one of the following flags defining the desired value:

`--criterion`: Choose which random forest criterion you wanna use. To see the options check the scikit-learn [docs](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html).

`--max_depth`: Choose the maximum depth of the random forest.
