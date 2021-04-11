import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Finding Outliers for all features using BoxPlot
def plotAllFeatureOutliers(df):
    numerical_feature = [feature for feature in df.columns if df[feature].dtypes != 'O']
    continuous_feature = [feature for feature in numerical_feature if len(df[feature].unique()) >= 25]
    for feature in continuous_feature:
        sns.boxplot(df[feature])
        plt.title(feature)
        plt.figure(figsize=(15, 15))
        plt.show()
# Finding Outliers for all features using BoxPlot

# Finding Outliers for specific feature using BoxPlot
def plotSpecificFeatureOutliers(df, feature):
    sns.boxplot(df[feature])
    plt.title(feature)
    plt.figure(figsize=(15, 15))
    plt.show()
# Finding Outliers for specific feature using BoxPlot

# Handling Outliers using IQR
def IQR(df, feature):
    IQR=df[feature].quantile(0.75)-df[feature].quantile(0.25)
    lower_bridge=df[feature].quantile(0.25)-(IQR*1.5)
    upper_bridge=df[feature].quantile(0.75)+(IQR*1.5)
    df.loc[df[feature]<=lower_bridge, feature]=lower_bridge
    df.loc[df[feature]>=upper_bridge, feature]=upper_bridge
# Handling Outliers using IQR

def handlingOutlierValues(df):
    numerical_feature = [feature for feature in df.columns if df[feature].dtypes != 'O']
    continuous_feature = [feature for feature in numerical_feature if len(df[feature].unique()) >= 25]
    plotting_outliers_all_or_specific = input("Do u want to find outliers using boxplot for all features or specific:\nall or specific\n")
    if "all" in plotting_outliers_all_or_specific:
        plotAllFeatureOutliers(df)
        print("All outliers plotted")
    elif "specific" in plotting_outliers_all_or_specific:
        feature = input("Enter the feature name correctly:\n")
        try:
            plotSpecificFeatureOutliers(df, feature)
            print("Specific plot for given feature is completed")
        except Exception:
            print("Please enter a valid feature")
    handling_outliers_yes_or_no = input("Do u want to handle outliers:\nYes or No\n")
    if "Yes" in handling_outliers_yes_or_no:
        handling_outliers_all_or_specific = input("Do u want to handle outliers of all features or specific feature:\nall or specific\n")
        if "all" in handling_outliers_all_or_specific:
            for feature in continuous_feature:
                IQR(df, feature)
        elif "specific" in handling_outliers_all_or_specific:
            feature = input("Enter the feature name correctly:\n")
            try:
                IQR(df, feature)
            except Exception:
                print("Please enter a valid feature")
        print("Outlier handle request completed")
        verification_outlier_yes_or_no = input("Do u want to verify by plotting boxplot again for all features:\nYes or No\n")
        if "Yes" in verification_outlier_yes_or_no:
            print("After handling Outliers:")
            plotAllFeatureOutliers(df)
        else:
            print("Ok")
    return (df)