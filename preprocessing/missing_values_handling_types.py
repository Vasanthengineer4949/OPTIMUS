import numpy as np
import pandas as pd

# Continuous Missing Values Handling Types

# Mean Imputation
def meanImputation(df, feature):
    mean = df[feature].mean()
    df[feature] = df[feature].fillna(mean)
# Mean Imputation

# Median Imputation
def medianImputation(df, feature):
    median = df[feature].median()
    df[feature] = df[feature].fillna(median)
# Median Imputation

# Random Sample Imputation
def randomSampleImputation(df, feature):
    df[feature] = df[feature]
    random_sample = df[feature].dropna().sample(df[feature].isnull().sum(), random_state=0)
    random_sample.index = df[df[feature].isnull()].index
    df.loc[df[feature].isnull(), feature] = random_sample
# Random Sample Imputation

# End of Distribution Imputation
def endOfDistributionImputation(df, feature):
    extreme = df[feature].mean() + 3 * df[feature].std()
    df[feature] = df[feature].fillna(extreme)
# End of Distribution Imputation

# Continuous Missing Values Handling Types

# Categorical Missing Values Handling Types

# Frequent Category Imputation
def frequentCategoryImputation(df,feature):
    most_frequent_category=df[feature].value_counts().index[0]
    df[feature].fillna(most_frequent_category,inplace=True)
# Frequent Category Imputation

# Capturing NaN with a new feature Imputation
def captureNaNwithFeatureImputation(df, feature):
    df[feature+"_new"] = np.where(df[feature].isnull(), 1, 0)
# Capturing NaN with a new feature Imputation

# Capturing NaN with a new category Imputation
def captureNaNwithCategoryImputation(df, feature):
    df[feature+"_new"]=np.where(df[feature].isnull(),"Missing",df[feature])
# Capturing NaN with a new category Imputation

# Categorical Missing Values Handling Types
