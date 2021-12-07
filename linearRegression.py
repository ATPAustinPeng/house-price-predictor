from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from myPCA import dimRed


def linReg(trainDf, testDf2):
    features = ['test_A']
    test_targets = testDf2.loc[:, ['price']].values
    test_feats = testDf2.loc[:, features].values
    test_feats = StandardScaler().fit_transform(test_feats)

    features = ['train_A']
    train_targets = trainDf.loc[:, ['price']].values
    train_feats = trainDf.loc[:, features].values
    train_feats = StandardScaler().fit_transform(train_feats)

    clf = LinearRegression(normalize=True)
    clf.fit(train_feats, train_targets)
    y_pred = clf.predict(test_feats)
    r2 = r2_score(test_targets, y_pred)

    normX = test_targets/np.linalg.norm(test_targets)
    normY = y_pred/np.linalg.norm(y_pred)

    mse = mean_squared_error(normX, normY)

    print(mse)
    print(r2)

    x = test_targets[0]
    y = y_pred[0]
    m, b = np.polyfit(x, y, 1)
    y = r2 * test_targets + b

    plt.plot(test_targets, y_pred, 'o', color="blue", label="")
    plt.plot(test_targets, y, color="black")
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.show()


if __name__ == '__main__':
    trainDf, testDf2 = dimRed()
    linReg(trainDf, testDf2)
