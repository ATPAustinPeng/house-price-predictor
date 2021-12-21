from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


def ridge_regression(trainDf, testDf):
    features = ['space', 'rooms', 'bedrooms',
                'furniture', 'latitude', 'longitude']
    test_targets = testDf.loc[:, ['price']].values
    test_feats = testDf.loc[:, features].values
    test_feats = StandardScaler().fit_transform(test_feats)

    train_targets = trainDf.loc[:, ['price']].values
    train_feats = trainDf.loc[:, features].values
    train_feats = StandardScaler().fit_transform(train_feats)

    model_ridge = Ridge()
    model_ridge.fit(train_feats, train_targets)
    pred_train_ridge = model_ridge.predict(train_feats)
    print("train r2_score", r2_score(train_targets, pred_train_ridge))

    pred_test_ridge = model_ridge.predict(test_feats)
    print("test r2_score ", r2_score(test_targets, pred_test_ridge))

    r2 = r2_score(test_targets, pred_test_ridge)
    normX = test_targets/np.linalg.norm(test_targets)
    normY = pred_test_ridge/np.linalg.norm(pred_test_ridge)

    mse = mean_squared_error(normX, normY)

    print("mse ", mse)
    print("r2 ", r2)

    x = test_targets
    x = x.reshape((x.shape[1], x.shape[0]))[0]
    y = pred_test_ridge
    y = y.reshape((1, y.shape[0]))[0]
    m, b = np.polyfit(x, y, 1)
    y = m * test_targets + b

    plt.plot(test_targets, pred_test_ridge, 'o', color="blue", label="")
    plt.plot(test_targets, y, color="black")
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title("Ridge Regression")
    plt.show()


if __name__ == "__main__":
    csvFile = []
    data = []
    with open('../preprocessing/preprocessed_data.csv', mode='r', encoding='UTF-8') as file:
        csvFile = csv.reader(file)
        count = 0
        for line in csvFile:
            if count != 0:
                data.append(line)
            count += 1
    data = np.array(data)
    data = np.float32(data)

    training_data, testing_data = train_test_split(
        data, test_size=0.2, random_state=25)

    trainDataDf = pd.DataFrame(training_data, columns=[
        'price', 'space', 'rooms', 'bedrooms', 'furniture', 'latitude', 'longitude'])
    testDataDf = pd.DataFrame(testing_data, columns=[
                              'price', 'space', 'rooms', 'bedrooms', 'furniture', 'latitude', 'longitude'])

    ridge_regression(trainDataDf, testDataDf)
