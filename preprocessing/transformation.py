import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

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
        elif "QQplot" in plot_features_type:
            qqplot_all_or_specific = input("Do you want plot for all features or a specific feature:\nall or specific\n")
            if "all" in qqplot_all_or_specific:
                for feature in continuous_feature:
                    distPlot(df, feature)
    transform_feature_type = input("How are you going to transform the features")

