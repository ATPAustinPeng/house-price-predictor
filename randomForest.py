import sklearn
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import csv
from rfPCA import dimRed

def ranFor(trainDf, testDf2):
    features = ['test_A','test_B','test_C']
    test_targets = testDf2.loc[:, ['price']].values
    test_feats = testDf2.loc[:, features].values
    test_feats = StandardScaler().fit_transform(test_feats)
    
    features = ['train_A', 'train_B', 'train_C']
    train_targets = trainDf.loc[:, ['price']].values
    train_feats = trainDf.loc[:, features].values
    train_feats = StandardScaler().fit_transform(train_feats)

    param_grid =  {'n_estimators':[200, 300, 400, 500, 600],
                'max_features':[0.1, 0.3, 0.6]
                }

    RandForest = RandomForestRegressor(n_jobs= -1, random_state = 0, bootstrap=True)

    Tuned_RandForest = GridSearchCV(estimator=RandForest, param_grid=param_grid, scoring='r2', cv=5)
    Tuned_RandForest.fit(train_feats, train_targets.ravel())

    # Results = pd.DataFrame(Tuned_RandForest.cv_results_)
    # Results_Best = Results.loc[Results.rank_test_score==2]
    print(Tuned_RandForest.best_score_)

if __name__ == '__main__':
    trainDf, testDf2 = dimRed()
    ranFor(trainDf, testDf2)