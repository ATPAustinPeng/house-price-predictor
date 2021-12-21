import sklearn
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


def dimension_reduction():
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

    dataDf = training_data
    testDataDf = testing_data
    dataDf = pd.DataFrame(training_data, columns=[
                          'price', 'space', 'room', 'bedroom', 'furniture', 'latitude', 'longitude'])
    testDataDf = pd.DataFrame(testing_data, columns=[
                              'price', 'space', 'room', 'bedroom', 'furniture', 'latitude', 'longitude'])

    features = ['space', 'room', 'bedroom',
                'furniture', 'latitude', 'longitude']
    feats = dataDf.loc[:, features].values
    feats = StandardScaler().fit_transform(feats)

    testFeats = testDataDf.loc[:, features].values
    testFeats = StandardScaler().fit_transform(testFeats)

    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(feats)
    testPC = pca.fit_transform(testFeats)

    print("pca features retained", np.cumsum(pca.explained_variance_ /
          np.sum(pca.explained_variance_))[0])

    df = pd.DataFrame(principalComponents, columns=['train_A', 'train_B'])
    testDf = pd.DataFrame(testPC, columns=['test_A', 'test_B'])

    trainDf = pd.concat([df, dataDf[["price"]]], axis=1)
    testDf2 = pd.concat([testDf, testDataDf[["price"]]], axis=1)
    return trainDf, testDf2
