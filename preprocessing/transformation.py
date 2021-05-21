import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import transformation_types

def distPlot(df, feature):
    print(feature)
    data = df.copy()
    sns.distplot(df[feature])
    plt.xlabel(feature)
    plt.ylabel("Count")
    plt.title(feature)
    plt.figure(figsize=(15, 15))
    plt.show()

def qqPlot(df, feature):
    print(feature)
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 2, 1)
    df[feature].hist()
    plt.subplot(1, 2, 2)
    stats.probplot(df[feature], dist="norm", plot=plt)
    plt.show()

def transformFeatures(df):
    numerical_feature = [feature for feature in df.columns if df[feature].dtypes != 'O']
    continuous_feature = [feature for feature in numerical_feature if len(df[feature].unique()) >= 25]
    plot_features_yes_or_no = input("Do u want to plot the continuous feature before transformation\nYes or No\n")
    if "Yes" in plot_features_yes_or_no:
        plot_features_type = input("How do u want the plot:\n Distplot or QQplot\n")
        if "Distplot" in plot_features_type:
            distplot_all_or_specific = input("Do you want plot for all features or a specific feature:\nall or specific\n")
            if "all" in distplot_all_or_specific:
                for feature in continuous_feature:
                    distPlot(df,feature)
            elif "specific" in distplot_all_or_specific:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    distPlot(df, feature)
                except Exception:
                    print("Please check the feature name")
        elif "QQplot" in plot_features_type:
            qqplot_all_or_specific = input("Do you want plot for all features or a specific feature:\nall or specific\n")
            if "all" in qqplot_all_or_specific:
                for feature in continuous_feature:
                    distPlot(df, feature)
            elif "specific" in qqplot_all_or_specific:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    qqPlot(df, feature)
                except Exception:
                    print("Please check the feature name")
    transform_feature_type = input("How are you going to transform the features:\n"
                                   "1-Normalization\n"
                                   "2-Standardization\n"
                                   "3-Robust Scaling\n"
                                   "4-Gaussian Transformation\n")
    if "1" in transform_feature_type:
        transform_feature_all_or_specific = input("Do u want to use this method to transform all or specific feature:\nall or specific\n")
        if "all" in transform_feature_all_or_specific:
            for feature in df.columns:
                transformation_types.normalization(df, feature)
        elif "specific" in transform_feature_all_or_specific:
            feature = input("Enter the correct name of the feature to be handled")
            try:
                transformation_types.normalization(df, feature)
            except Exception:
                print("Please check the feature name")

    elif "2" in transform_feature_type:
        transform_feature_all_or_specific = input("Do u want to use this method to transform all or specific feature:\nall or specific\n")
        if "all" in transform_feature_all_or_specific:
            for feature in df.columns:
                transformation_types.standardization(df, feature)
        elif "specific" in transform_feature_all_or_specific:
            feature = input("Enter the correct name of the feature to be handled")
            try:
                transformation_types.standardization(df, feature)
            except Exception:
                print("Please check the feature name")

    elif "3" in transform_feature_type:
        transform_feature_all_or_specific = input("Do u want to use this method to transform all or specific feature:\nall or specific\n")
        if "all" in transform_feature_all_or_specific:
            for feature in df.columns:
                transformation_types.robustScaling(df, feature)
        elif "specific" in transform_feature_all_or_specific:
            feature = input("Enter the correct name of the feature to be handled")
            try:
                transformation_types.robustScaling(df, feature)
            except Exception:
                print("Please check the feature name")

    elif "4" in transform_feature_type:
        gaussian_transform_feature_type = input("What type of Gaussian Transformation do you want to perform:\n"
                                       "1-Logarithmic Transformation\n"
                                       "2-Exponential Transformation\n"
                                       "3-Reciprocal Transformation\n"
                                       "4-Square Transformation\n"
                                       "5-Boxcox Transformation\n")
        if "1" in gaussian_transform_feature_type:
            gaussian_transform_feature_all_or_specific = input("Do u want to use this method to transform all or specific feature:\nall or specific\n")
            if "all" in gaussian_transform_feature_all_or_specific:
                for feature in df.columns:
                    transformation_types.logarithmic(df, feature)
            elif "specific" in gaussian_transform_feature_all_or_specific:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    transformation_types.logarithmic(df, feature)
                except Exception:
                    print("Please check the feature name")

        elif "2" in gaussian_transform_feature_type:
            gaussian_transform_feature_all_or_specific = input("Do u want to use this method to transform all or specific feature:\nall or specific\n")
            if "all" in gaussian_transform_feature_all_or_specific:
                for feature in df.columns:
                    transformation_types.exponential(df, feature)
            elif "specific" in gaussian_transform_feature_all_or_specific:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    transformation_types.exponential(df, feature)
                except Exception:
                    print("Please check the feature name")

        elif "3" in gaussian_transform_feature_type:
            gaussian_transform_feature_all_or_specific = input("Do u want to use this method to transform all or specific feature:\nall or specific\n")
            if "all" in gaussian_transform_feature_all_or_specific:
                for feature in df.columns:
                    transformation_types.reciprocal(df, feature)
            elif "specific" in gaussian_transform_feature_all_or_specific:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    transformation_types.reciprocal(df, feature)
                except Exception:
                    print("Please check the feature name")

        elif "4" in gaussian_transform_feature_type:
            gaussian_transform_feature_all_or_specific = input("Do u want to use this method to transform all or specific feature:\nall or specific\n")
            if "all" in gaussian_transform_feature_all_or_specific:
                for feature in df.columns:
                    transformation_types.square(df, feature)
            elif "specific" in gaussian_transform_feature_all_or_specific:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    transformation_types.square(df, feature)
                except Exception:
                    print("Please check the feature name")

        elif "5" in gaussian_transform_feature_type:
            gaussian_transform_feature_all_or_specific = input("Do u want to use this method to transform all or specific feature:\nall or specific\n")
            if "all" in gaussian_transform_feature_all_or_specific:
                for feature in df.columns:
                    transformation_types.boxcox(df, feature)
            elif "specific" in gaussian_transform_feature_all_or_specific:
                feature = input("Enter the correct name of the feature to be handled")
                try:
                    transformation_types.boxcox(df, feature)
                except Exception:
                    print("Please check the feature name")

        plot_features_again_yes_or_no = input("Do u want to plot the continuous feature before transformation\nYes or No\n")
        if "Yes" in plot_features_again_yes_or_no:
            plot_features_type = input("How do u want the plot:\n Distplot or QQplot\n")
            if "Distplot" in plot_features_type:
                distplot_all_or_specific = input(
                    "Do you want plot for all features or a specific feature:\nall or specific\n")
                if "all" in distplot_all_or_specific:
                    for feature in continuous_feature:
                        distPlot(df, feature)
                elif "specific" in distplot_all_or_specific:
                    feature = input("Enter the correct name of the feature to be handled")
                    try:
                        distPlot(df, feature)
                    except Exception:
                        print("Please check the feature name")
            elif "QQplot" in plot_features_type:
                qqplot_all_or_specific = input(
                    "Do you want plot for all features or a specific feature:\nall or specific\n")
                if "all" in qqplot_all_or_specific:
                    for feature in continuous_feature:
                        distPlot(df, feature)
                elif "specific" in qqplot_all_or_specific:
                    feature = input("Enter the correct name of the feature to be plotted")
                    try:
                        qqPlot(df, feature)
                    except Exception:
                        print("Please check the feature name")
        else:
            print("Ok")



