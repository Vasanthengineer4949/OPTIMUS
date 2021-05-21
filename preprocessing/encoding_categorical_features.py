import numpy as np
import pandas as pd
import encoding_categorical_features_types
def encodingCategoricalValues(df):
    numerical_feature = [feature for feature in df.columns if df[feature].dtypes != 'O']
    discrete_feature = [feature for feature in numerical_feature if len(df[feature].unique()) < 25]
    continuous_feature = [feature for feature in numerical_feature if feature not in discrete_feature]
    categorical_feature = [feature for feature in df.columns if feature not in numerical_feature]
    encoding_type = input("How do you want to encode the categorical feature:\n"
                          "1 - One Hot Encoding\n"
                          "2 - Label Encoding\n"
                          "3 - Ordinal Number Encoding(for Date column)\n"
                          "4 - Count or Frequency Encoding\n"
                          "5 - Target Guided Ordinal Encoding\n"
                          "6 - Target Guided Mean Encoding\n")
    if "1" in encoding_type:
        encoding_type_for_all = input("Do you want to implement this encoding to all feature or specific feature\n")
        if "all" in encoding_type_for_all:
            for feature in categorical_feature:
                encoding_categorical_features_types.oneHotEncoding(df, feature)
        elif "specific" in encoding_type_for_all:
            feature = input("Enter the correct name of the feature to be encoded")
            try:
                encoding_categorical_features_types.oneHotEncoding(df, feature)
            except Exception:
                print("Please check the feature name")
    elif "2" in encoding_type:
        encoding_type_for_all = input("Do you want to implement this encoding to all feature or specific feature\n")
        if "all" in encoding_type_for_all:
            for feature in categorical_feature:
                encoding_categorical_features_types.labelEncoding(df, feature)
        elif "specific" in encoding_type_for_all:
            feature = input("Enter the correct name of the feature to be encoded")
            try:
                encoding_categorical_features_types.labelEncoding(df, feature)
            except Exception:
                print("Please check the feature name")
    elif "3" in encoding_type:
        print("Under Development")
        # encoding_type_for_all = input("Do you want to implement this encoding to all feature or specific feature")
        # if "all" in encoding_type_for_all:
        #     for feature in categorical_feature:
        #         encoding_categorical_features_types.dateOrdinalEncoding(df, feature)
        # elif "specific" in encoding_type_for_all:
        #     feature = input("Enter the correct name of the feature to be encoded")
        #     try:
        #         encoding_categorical_features_types.dateOrdinalEncoding(df, feature)
        #     except Exception:
        #         print("Please check the feature name")
    elif "4" in encoding_type:
        encoding_type_for_all = input("Do you want to implement this encoding to all feature or specific feature\n")
        if "all" in encoding_type_for_all:
            for feature in categorical_feature:
                encoding_categorical_features_types.countEncoding(df, feature)
        elif "specific" in encoding_type_for_all:
            feature = input("Enter the correct name of the feature to be encoded")
            try:
                encoding_categorical_features_types.countEncoding(df, feature)
            except Exception:
                print("Please check the feature name")
    elif "5" in encoding_type:
        dependent_feature = input("Enter the name of the dependent feature correctly\n")
        encoding_type_for_all = input("Do you want to implement this encoding to all feature or specific feature\n")
        if "all" in encoding_type_for_all:
            for feature in categorical_feature:
                encoding_categorical_features_types.targetGuidedOrdinalEncoding(df, feature, dependent_feature)
        elif "specific" in encoding_type_for_all:
            feature = input("Enter the correct name of the feature to be encoded")
            try:
                encoding_categorical_features_types.targetGuidedOrdinalEncoding(df, feature, dependent_feature)
            except Exception:
                print("Please check the feature name")
    elif "6" in encoding_type:
        dependent_feature = input("Enter the name of the dependent feature correctly\n")
        encoding_type_for_all = input("Do you want to implement this encoding to all feature or specific feature\n")
        if "all" in encoding_type_for_all:
            for feature in categorical_feature:
                encoding_categorical_features_types.targetGuidedMeanEncoding(df, feature, dependent_feature)
        elif "specific" in encoding_type_for_all:
            feature = input("Enter the correct name of the feature to be encoded")
            try:
                encoding_categorical_features_types.targetGuidedMeanEncoding(df, feature, dependent_feature)
            except Exception:
                print("Please check the feature name")
    return(df)