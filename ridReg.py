from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from myPCA import dimRed

from sklearn.linear_model import Lasso

def ridReg(trainDf, testDf2):
    features = ['test_A']
    test_targets = testDf2.loc[:, ['price']].values
    test_feats = testDf2.loc[:, features].values
    test_feats = StandardScaler().fit_transform(test_feats)
    
    features = ['train_A']
    train_targets = trainDf.loc[:, ['price']].values
    train_feats = trainDf.loc[:, features].values
    train_feats = StandardScaler().fit_transform(train_feats)
    
    # params = {'alpha': [0.0001, 0.001, 0.01, 0.05, 0.1, 
    # 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 2.0, 3.0, 
    # 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]}

    # ridge = Ridge()
    # folds = 5
    # model_cv = GridSearchCV(estimator=ridge,
    #                     param_grid=params,
    #                     scoring='r2',
    #                     cv=folds,
    #                     return_train_score=True,
    #                     verbose=1)
    # model_cv.fit(train_feats, train_targets)
    # ridge_results = pd.DataFrame(model_cv.cv_results_)
    # print(model_cv.best_score_)

    # ridge_results['param_alpha'] = ridge_results['param_alpha'].astype('int32')
    # plt.figure(figsize=(8,6))
    # plt.plot(ridge_results['param_alpha'], ridge_results['mean_train_score'])
    # plt.plot(ridge_results['param_alpha'], ridge_results['mean_test_score'])
    # plt.legend(['train score', 'test score'])
    # plt.xlabel('alpha')
    # plt.ylabel('mean r2 score')
    # plt.show()

    # model_ridge = Ridge(alpha=2)
    # model_ridge.fit(train_feats, train_targets)
    # y_train_pred = model_ridge.predict(train_feats)
    # print(r2_score(y_true = train_targets, y_pred = y_train_pred))
    # y_test_pred = model_ridge.predict(test_feats)
    # print(r2_score(y_true = test_targets, y_pred = y_test_pred))

    model_lasso = Lasso(alpha=0.01)
    model_lasso.fit(train_feats, train_targets) 
    pred_train_lasso= model_lasso.predict(train_feats)
    print(r2_score(train_targets, pred_train_lasso))

    pred_test_lasso= model_lasso.predict(test_feats)
    print(r2_score(test_targets, pred_test_lasso))

if __name__ == '__main__':
    trainDf, testDf2 = dimRed()
    ridReg(trainDf, testDf2)
