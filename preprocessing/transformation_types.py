import numpy as np
import pandas as pd

def normalization(df, feature):
    from sklearn.preprocessing import MinMaxScaler
    normalScaler = MinMaxScaler()
    df[feature] = normalScaler.fit_transform(np.array(df[feature]).reshape(-1, 1))

def standardization(df, feature):
    from sklearn.preprocessing import StandardScaler
    standardScaler = StandardScaler()
    df[feature] = standardScaler.fit_transform(np.array(df[feature]).reshape(-1, 1))

def robustScaling(df, feature):
    from sklearn.preprocessing import RobustScaler
    robustScaler = RobustScaler()
    df[feature] = robustScaler.fit_transform(np.array(df[feature]).reshape(-1, 1))

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
    try:
        from scipy import stats as stats
        df[feature], param = stats.boxcox(df[feature])
    except ValueError:
        print("U have negative or else constant value in your data."
              " So this method cannot be used. Try another method")