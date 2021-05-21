import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import missing_values_handling_types

# Missing Values
def missing_values_feature(df):
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]
    return missing_values
# Missing Values

# Checking the missing values percentage in the dataframe
def check_missing_values_percentage(df):
    print("The total percentage of missing values in the dataset is:")
    missing_values_percentage = (df.isnull().sum()/len(df))*100
    print(missing_values_percentage)
# Checking the missing values percentage in the dataframe

# Heatmap for plotting missing values
def missing_values_heatmap(df):
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis", linecolor="red")
    plt.show()
# Heatmap for plotting missing values

# Barplot for plotting missing values
def missing_values_barplot(df):
    missing_values = missing_values_feature(df)
    missing_values.sort_values(inplace=True)
    missing_values = missing_values.to_frame()
    missing_values.columns = ['count']
    missing_values.index.names = ['Name']
    missing_values['Name'] = missing_values.index
    sns.set(style="whitegrid", color_codes=True)
    sns.barplot(x='Name', y='count', data=missing_values)
    plt.xticks(rotation=90)
    plt.show()
# Barplot for plotting missing values

# Handling the missing values

def missing_values_handling(df):
    numerical_feature = [feature for feature in df.columns if df[feature].dtypes != 'O']
    discrete_feature = [feature for feature in numerical_feature if len(df[feature].unique()) < 25]
    continuous_feature = [feature for feature in numerical_feature if feature not in discrete_feature]
    categorical_feature = [feature for feature in df.columns if feature not in numerical_feature]
    check_missing_values_percentage(df)

    # Plotting the missing values
    plot_missing = input("Do u want to plot missing values features:\nYes or No \n")
    if "Yes" in plot_missing:
        plot_missing_type = input("What plot do u want:\nHeatmap of Barplot\n")
        if "Heatmap" in plot_missing_type:
            missing_values_heatmap(df)
        elif "Barplot" in plot_missing_type:
            missing_values_barplot(df)
    type_missing = input("How do you want to handle the missing values?\nDrop or Fill \n")
    # Plotting the missing values

    # Dropping the missing values
    if "Drop" in type_missing:
        missing_values = missing_values_feature(df)
        df_missing_dropped = df.dropna(inplace=True)
        print("After dropping")
        missing_values_percentage = (df.isnull().sum() / len(df)) * 100
        print(missing_values_percentage)
    # Dropping the missing values

    # Filling the missing values
    elif "Fill" in type_missing:

        # Filling the continuous missing values
        fill_missing_type_continuous = input("How do u want to handle continuous missing values features:"
                                 "\nMean imputation-1\nMedian imputation-2\nRandom Sample Imputation-3\n"
                                 "End of Distribution Imputation-4\n")

        if "1" in fill_missing_type_continuous:
            missing_handling_for_all = input("Do you want to implement this handling to all feature or specific feature\n")
            if "all" in missing_handling_for_all:
                for feature in continuous_feature:
                    missing_values_handling_types.meanImputation(df, feature)
            elif "specific" in missing_handling_for_all:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    missing_values_handling_types.meanImputation(df, feature)
                except Exception:
                    print("Please check the feature name")

        if "2" in fill_missing_type_continuous:
            missing_handling_for_all = input("Do you want to implement this handling to all feature or specific feature\n")
            if "all" in missing_handling_for_all:
                for feature in continuous_feature:
                    missing_values_handling_types.medianImputation(df, feature)
            elif "specific" in missing_handling_for_all:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    missing_values_handling_types.medianImputation(df, feature)
                except Exception:
                    print("Please check the feature name")

        if "3" in fill_missing_type_continuous:
            missing_handling_for_all = input("Do you want to implement this handling to all feature or specific feature\n")
            if "all" in missing_handling_for_all:
                for feature in continuous_feature:
                    missing_values_handling_types.randomSampleImputation(df, feature)
            elif "specific" in missing_handling_for_all:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    missing_values_handling_types.randomSampleImputation(df, feature)
                except Exception:
                    print("Please check the feature name")

        if "4" in fill_missing_type_continuous:
            missing_handling_for_all = input("Do you want to implement this handling to all feature or specific feature\n")
            if "all" in missing_handling_for_all:
                for feature in continuous_feature:
                    missing_values_handling_types.endOfDistributionImputation(df, feature)
            elif "specific" in missing_handling_for_all:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    missing_values_handling_types.endOfDistributionImputation(df, feature)
                except Exception:
                    print("Please check the feature name")
        print("After handling")
        missing_values_percentage = (df.isnull().sum() / len(df)) * 100
        print(missing_values_percentage)
        # Filling the continuous missing values

        # Filling the discrete missing values
        fill_missing_type_discrete = input("Do u want to handle discrete missing values features:"
                                              "\nMode Imputation-1\n")
        if "1" in fill_missing_type_discrete:
            missing_handling_for_all = input("Do you want to implement this handling to all feature or specific feature\n")
            if "all" in missing_handling_for_all:
                for feature in discrete_feature:
                    missing_values_handling_types.frequentCategoryImputation(df, feature)
            elif "specific" in missing_handling_for_all:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    missing_values_handling_types.frequentCategoryImputation(df, feature)
                except Exception:
                    print("Please check the feature name")
        # Filling the discrete missing values

        # Filling the categorical missing values
        fill_missing_type_categorical = input("How do u want to handle categorical missing values features:"
                                              "\nMode Imputation-1\nCapturing NAN value with new feature Imputation-2\n"
                                              "Capturing NAN value with new category Imputation-2-3\n")
        if "1" in fill_missing_type_categorical:
            missing_handling_for_all = input("Do you want to implement this handling to all feature or specific feature\n")
            if "all" in missing_handling_for_all:
                for feature in categorical_feature:
                    missing_values_handling_types.frequentCategoryImputation(df, feature)
            elif "specific" in missing_handling_for_all:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    missing_values_handling_types.frequentCategoryImputation(df, feature)
                except Exception:
                    print("Please check the feature name")

        if "2" in fill_missing_type_categorical:
            missing_handling_for_all = input("Do you want to implement this handling to all feature or specific feature\n")
            if "all" in missing_handling_for_all:
                for feature in categorical_feature:
                    missing_values_handling_types.captureNaNwithFeatureImputation(df, feature)
            elif "specific" in missing_handling_for_all:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    missing_values_handling_types.captureNaNwithFeatureImputation(df, feature)
                except Exception:
                    print("Please check the feature name")

        if "3" in fill_missing_type_categorical:
            missing_handling_for_all = input("Do you want to implement this handling to all feature or specific feature\n")
            if "all" in missing_handling_for_all:
                for feature in categorical_feature:
                    missing_values_handling_types.captureNaNwithCategoryImputation(df, feature)
            elif "specific" in missing_handling_for_all:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    missing_values_handling_types.captureNaNwithCategoryImputation(df, feature)
                except Exception:
                    print("Please check the feature name")
        # Filling the categorical missing values
        return(df)
# Handling the missing values