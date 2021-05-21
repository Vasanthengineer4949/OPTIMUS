import pandas as pd


# Variance Threshold method
def varianceThreshold(X, threshold=0):
    from sklearn.feature_selection import VarianceThreshold
    varianceThresholdSelector = VarianceThreshold(threshold=float(threshold))
    varianceThresholdSelector.fit(X)
    selectedColumns = X.columns[varianceThresholdSelector.get_support()]
    removedColumns = [column for column in X.columns if
                      column not in X.columns[varianceThresholdSelector.get_support()]]
    removedColumnsCount = len(removedColumns)
    print("The columns selected are:", selectedColumns)
    print("The columns selected are:", removedColumns)
    print("Number of columns removed", removedColumnsCount)
    updateDf = input("Do u want to remove the low variance columns in the dataset:\nYes or No\n")
    if "Yes" in updateDf:
        X = X[selectedColumns]
    else:
        pass

# Variance Threshold method

# Pearson correlation method
def pearsonCorrelation(X, threshold=0.8):
    correlatedColumns = []  # Set of all the names of correlated columns
    correlationMatrix = X.corr()
    features = X.columns.to_list()
    for i in range(len(correlationMatrix.columns)):
        for j in range(i):
            if abs(correlationMatrix.iloc[i, j]) > float(threshold):
                correlatedColumn = correlationMatrix.columns[i]
                correlatedColumns.append(correlatedColumn)
    updateDf = input("Do u want to remove the correlated features in the dataset\nYes or No\n")
    if "Yes" in updateDf:
        X = X.drop(correlatedColumns, axis=1)
    else:
        pass
    selectedColumns = [column for column in X.columns if column not in correlatedColumns]
    removedColumns = correlatedColumns
    removedColumnsCount = len(removedColumns)
    pearsonCorrelationSupport = [True if i in correlatedColumns else False for i in features]
    print("The columns selected are:", selectedColumns)
    print("The columns removed are:", removedColumns)
    print("Number of columns removed", removedColumnsCount)
    return pearsonCorrelationSupport, selectedColumns, removedColumns, removedColumnsCount

# Pearson correlation method

# Chi Square method
def chiSquare(X, y, num_feats):
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import chi2
    chiSelector = SelectKBest(chi2, k=int(num_feats))
    chiSelector.fit(X, y)
    chiSquareSupport = chiSelector.get_support()
    selectedColumns = X.loc[:, chiSquareSupport].columns.tolist()
    removedColumns = [column for column in X.columns if column not in selectedColumns]
    removedColumnsCount = len(removedColumns)
    print("The columns selected are:", selectedColumns)
    print("The columns removed are:", removedColumns)
    print("Number of columns removed", removedColumnsCount)
    updateDf = input("Do u want to update the dataset to the features selected\nYes or No\n")
    if "Yes" in updateDf:
        X = X[selectedColumns]
    else:
        pass
    return chiSquareSupport, selectedColumns, removedColumns, removedColumnsCount

# Chi Square method

# Lasso model
def lassoSelectFromModel(X, y, alpha=0.01):
    from sklearn.linear_model import Lasso
    from sklearn.feature_selection import SelectFromModel
    lassoSelector = SelectFromModel(Lasso(alpha=0.001, random_state=0))
    lassoSelector.fit(X, y)
    lassoSelectorSupport = lassoSelector.get_support()
    selectedColumns = X.loc[:, lassoSelector].columns.tolist()
    removedColumns = [column for column in X.columns if column not in selectedColumns]
    removedColumnsCount = len(removedColumns)
    print("The columns selected are:", selectedColumns)
    print("The columns removed are:", removedColumns)
    print("Number of columns removed", removedColumnsCount)
    updateDf = input("Do u want to update the dataset to the features selected\nYes or No\n")
    if "Yes" in updateDf:
        X = X[selectedColumns]
    else:
        pass
    return lassoSelectorSupport, removedColumns, removedColumnsCount

# Lasso model

# Logistic model
def logisticSelectFromModel(X, y, num_feats):
    from sklearn.feature_selection import SelectFromModel
    from sklearn.linear_model import LogisticRegression
    logisticSelector = SelectFromModel(
        LogisticRegression(), max_features=int(num_feats))
    logisticSelector.fit(X, y)
    logisticSelectorSupport = logisticSelector.get_support()
    selectedColumns = X.loc[:, logisticSelector].columns.tolist()
    removedColumns = [column for column in X.columns if column not in selectedColumns]
    removedColumnsCount = len(removedColumns)
    print("The columns selected are:", selectedColumns)
    print("The columns removed are:", removedColumns)
    print("Number of columns removed", removedColumnsCount)
    updateDf = input("Do u want to update the dataset to the features selected\nYes or No\n")
    if "Yes" in updateDf:
        X = X[selectedColumns]
    else:
        pass
    return logisticSelectorSupport, removedColumns, removedColumnsCount

# Logistic model

# Tree Based model
def treeBasedSelectFromModel(X, y, num_feats):
    # global estimator
    from sklearn.feature_selection import SelectFromModel
    tree_type = input("What tree based model do you want to use:\n"
                      "1-RandomForest\n"
                      "2-GradientBoosting\n"
                      "3-LightGBM\n"
                      "4-Xgboost\n"
                      "5-Catboost")
    if "1" in tree_type:
        from sklearn.ensemble import RandomForestClassifier
        estimator = RandomForestClassifier(n_estimators=100,
                                           random_state=0,
                                           n_jobs=-1, verbose=1)
    elif "2" in tree_type:
        from sklearn.ensemble import GradientBoostingClassifier
        estimator = GradientBoostingClassifier(n_estimators=100,
                                               learning_rate=0.05,
                                               max_depth=5,
                                               random_state=0)
    elif "3" in tree_type:
        from lightgbm import LGBMClassifier
        estimator = LGBMClassifier(n_estimators=500,
                                   learning_rate=0.05,
                                   num_leaves=32,
                                   colsample_bytree=0.2,
                                   reg_alpha=3,
                                   reg_lambda=1,
                                   min_split_gain=0.01,
                                   min_child_weight=40)
    elif "4" in tree_type:
        from xgboost import XGBClassifier
        estimator = XGBClassifier(max_depth=5,
                                  learning_rate=0.01,
                                  n_estimators=100,
                                  gamma=0,
                                  min_child_weight=1,
                                  subsample=0.8,
                                  colsample_bytree=0.8,
                                  reg_alpha=0.005)
    elif "5" in tree_type:
        from catboost import CatBoostClassifier
        estimator = CatBoostClassifier(iterations=1000,
                                       learning_rate=0.01)
    treeBasedSelector = SelectFromModel(estimator, max_features=int(num_feats))
    treeBasedSelector.fit(X, y)
    treeSelectorSupport = treeBasedSelector.get_support()
    selectedColumns = X.loc[:, treeBasedSelector].columns.tolist()
    removedColumns = [column for column in X.columns if column not in selectedColumns]
    removedColumnsCount = len(removedColumns)
    print("The columns selected are:", selectedColumns)
    print("The columns removed are:", removedColumns)
    print("Number of columns removed", removedColumnsCount)
    updateDf = input("Do u want to update the dataset to the features selected\nYes or No\n")
    if "Yes" in updateDf:
        X = X[selectedColumns]
    else:
        pass
    return treeSelectorSupport, removedColumns, removedColumnsCount

# Tree Based model
