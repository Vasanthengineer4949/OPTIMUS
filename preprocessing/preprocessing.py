import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missing_values
import encoding_categorical_features
import outlier_handling
import transformation
import feature_selection

# Reading the dataframe
path_to_csv = input("Enter the path to the csv file \n")
df = pd.read_csv(path_to_csv)
pd.set_option("display.max_columns", None)
print(df)
# Reading the dataframe

# # Classification of number of features
# print("The feature is classified as")
# numerical_feature = [feature for feature in df.columns if df[feature].dtypes != 'O']
# discrete_feature = [feature for feature in numerical_feature if len(df[feature].unique()) < 25]
# continuous_feature = [feature for feature in numerical_feature if feature not in discrete_feature]
# categorical_feature = [feature for feature in df.columns if feature not in numerical_feature]
# print("Numerical feature:", numerical_feature)
# print("Discrete Numerical feature:", discrete_feature)
# print("Continuous Numerical feature:", continuous_feature)
# print("Categorical feature:", categorical_feature)
# # Classification of number of features
#
# # Dropping the unnecessary features
# drop_features_yes_or_no = input("Do you want to drop any features:\nYes or No\n")
# if "Yes" in drop_features_yes_or_no:
#     drop_features_list = input("What are the features you want to drop?\nType in this format:\n"
#                                "feature1 feature2 feature3 ...").split()
#     df.drop(drop_features_list, axis=1, inplace=True)
#     print(df)
#     print("Ok lets move to the next step")
# else:
#     print("Ok lets move to the next step")
# # Dropping the unnecessary features
#
# # Missing values handling
# missing_yes_or_no = input("Do you want find missing values:\nYes or No\n")
# if "Yes" in missing_yes_or_no:
#     missing_values.missing_values_handling(df)
#     print("After handling")
#     missing_values_percentage = (df.isnull().sum() / len(df)) * 100
#     print(missing_values_percentage)
#     print("Ok lets move to the next step")
# else:
#     print("Ok lets move to the next step")
# # Missing values handling
#
# # Handling Categorical Features
# categorical_handling_yes_or_no = input("Do you want to handle categorical values:\nYes or No\n")
# if "Yes" in categorical_handling_yes_or_no:
#     encoding_categorical_features.encodingCategoricalValues(df)
#     print("After encoding")
#     print(df)
#     print("Ok lets move to the next step")
# else:
#     print("Ok lets move to the next step")
# # Handling Categorical Features
#
# # Handling Outlier
# outlier_handling_yes_or_no = input("Do you want to find outliers:\nYes or No\n")
# if "Yes" in outlier_handling_yes_or_no:
#     outlier_handling.handlingOutlierValues(df)
#     print("Ok lets move to the next step")
# else:
#     print("Ok lets move to the next step")
#
# # Handling Outliers
#
# # df.to_csv("preprocessed.csv", index=False)
#
# # Transformation of Data
# transforming_data_yes_or_no = input("Do you want to perform transformations on data:\nYes or No\n")
# if "Yes" in transforming_data_yes_or_no:
#     transformation.transformFeatures(df)
#     print_transformed_yes_or_no = input("Do you want to see the dataset after transformation:\nYes or No\n")
#     if "Yes" in print_transformed_yes_or_no:
#         print(df)
#         print("Ok lets move to the next step")
#     else:
#         pass
# else:
#     print("Ok lets move to the next step")
# # Transformation of Data

# Feature Selection
feature_selection_yes_or_no = input("Do you want to perform feature selection in this data:\nYes or No\n")
if "Yes" in feature_selection_yes_or_no:
    outputFeature = input("Enter the correct name of the output feature")
    y = df[outputFeature]
    X = df.drop([outputFeature], axis=1)
    feature_selection.featureSelection(X, y)
    print(X)
# Feature Selection

