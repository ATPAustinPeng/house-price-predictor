from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import csv


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

    dataDf = pd.DataFrame(training_data, columns=[
                          'id', 'views', 'price', 'space', 'rooms', 'latitude', 'longitude'])
    testDataDf = pd.DataFrame(testing_data, columns=[
                              'id', 'views', 'price', 'space', 'rooms', 'latitude', 'longitude'])

    features = ['views', 'space', 'rooms', 'latitude', 'longitude']
    # target = dataDf.loc[:, ['price']].values
    feats = dataDf.loc[:, features].values
    feats = StandardScaler().fit_transform(feats)

    # testTarget = testDataDf.loc[:, ['price']].values
    testFeats = testDataDf.loc[:, features].values
    testFeats = StandardScaler().fit_transform(testFeats)

    pca = PCA(n_components=3)
    principalComponents = pca.fit_transform(feats)
    testPC = pca.fit_transform(testFeats)
    df = pd.DataFrame(principalComponents, columns=[
                      'train_A', 'train_B', 'train_C'])
    testDf = pd.DataFrame(testPC, columns=['test_A', 'test_B', 'test_C'])

    trainDf = pd.concat([df, dataDf[["price"]]], axis=1)
    testDf2 = pd.concat([testDf, testDataDf[["price"]]], axis=1)
    return trainDf, testDf2
