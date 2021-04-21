import pandas as pd

def normalization(df, feature):
    from sklearn.preprocessing import MinMaxScaler
    normalScaler = MinMaxScaler()
    normalScaler.fit_transform(df[feature])

def standardization(df, feature):
    from sklearn.preprocessing import StandardScaler
    standardScaler = StandardScaler()
    standardScaler.fit_transform(df[feature])

def robustScaling(df, feature):
    from sklearn.preprocessing import RobustScaler
    robustScaler = RobustScaler()
    robustScaler.fit_transform(df[feature])

def logarithmic(df, feature):
    import numpy as np
    df[feature] = np.log(df[feature] + 1)

def exponential(df, feature):
    df[feature] = df[feature] ** 0.2

def reciprocal(df, feature):
    df[feature] = 1 / (df[feature] + 1)

def square(df, feature):
    df[feature] = df[feature] ** 0.5

def boxcox(df, feature):
    from scipy import stats as stats
    df[feature], param = stats.boxcox(df[feature] + 1)