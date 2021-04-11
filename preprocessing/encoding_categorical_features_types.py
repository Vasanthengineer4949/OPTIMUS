import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import datetime
# One Hot Encoding
def oneHotEncoding(df, feature):
    df[feature] = pd.get_dummies(df[feature], drop_first=True)
# One Hot Encoding

# Label Encoding
def labelEncoding(df, feature):
    lbl = LabelEncoder()
    lbl.fit(list(df[feature].values))
    df[feature] = lbl.transform(list(df[feature].values))
# Label Encoding

# Count or Frequency Encoding
def countEncoding(df, feature):
    feature_map = df[feature].value_counts().to_dict()
    df['Country'] = df[feature].map(feature_map)
# Count or Frequency Encoding

# Target Guided Ordinal Encoding
def targetGuidedOrdinalEncoding(df, feature, dependent_feature):
    feature_label = df.groupby([feature])[dependent_feature].mean().sort_values().index
    feature_label2 = {k: i for i, k in enumerate(feature_label, 0)}
    df[feature] = df[feature].map(feature_label2)
# Target Guided Ordinal Encoding

# Target Guided Mean Encoding
def targetGuidedMeanEncoding(df, feature, dependent_feature):
    feature_mean_label = df.groupby([feature])[dependent_feature].mean().to_dict()
    df[feature] = df[feature].map(feature_mean_label)
# Target Guided Mean Encoding