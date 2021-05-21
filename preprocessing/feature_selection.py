import numpy as np
import pandas as pd
import feature_selection_types

def featureSelection(X, y):
    feature_selection_type = input("What type of feature selection do you want to perform\n"
                                   "1-Variance Threshold\n"
                                   "2-Pearson Correlation\n"
                                   "3-Chi Square Test\n"
                                   "4-Lasso Regressor\n"
                                   "5-Logistic Regression based SelectFromModel\n"
                                   "6-Tree based SelectFromModel\n"
                                   "7-Recursive Feature Elimination\n"
                                   "8-Perform all these and come to a decision\n")
    if "1" in feature_selection_type:
        threshold_input = input("Enter the threshold value for variance in columns to be checked\n"
                                "Value range- 0 to 1\n")
        feature_selection_types.varianceThreshold(X, threshold_input)
    elif "2" in feature_selection_type:
        threshold_input = input("Enter the threshold value for correlation in columns to be checked\n"
                                "Value range- 0 to 1\n")
        feature_selection_types.pearsonCorrelation(X, threshold_input)
    elif "3" in feature_selection_type:
            num_feats = input("Enter the number of features to be selected")
            feature_selection_types.chiSquare(X, y, num_feats)
            print(X)
    elif "4" in feature_selection_type:
        alpha = input("Enter the alpha value")
        feature_selection_types.lassoSelectFromModel(X, y, alpha)
        print(X)
    elif "5" in feature_selection_type:
        num_feats = input("Enter the maximum number of features you need to have")
        feature_selection_types.logisticSelectFromModel(X, y, num_feats)
        print(X)
    elif "6" in feature_selection_type:
        num_feats = input("Enter the maximum number of features you need to have")
        feature_selection_types.treeBasedSelectFromModel(X, y, num_feats=num_feats)
        print(X)
