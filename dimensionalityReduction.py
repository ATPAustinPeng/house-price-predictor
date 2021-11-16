from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import csv

def dimRed():
    csvFile = []
    data = []
    with open('clean_data.csv', mode ='r', encoding = 'UTF-8') as file:     
        csvFile = csv.reader(file) 
        count = 0
        for line in csvFile:
            if count != 0:
                data.append(line)
            count+=1
    data = np.array(data)
    data = np.float32(data)

    training_data, testing_data = train_test_split(data, test_size=0.2, random_state=25)
    # print(f"No. of training examples: {training_data.shape[0]}")
    # print(f"No. of testing examples: {testing_data.shape[0]}")

    dataDf = pd.DataFrame(training_data, columns = ['id','views', 'price', 'space', 'rooms', 'latitude', 'longitude'])
    testDataDf = pd.DataFrame(testing_data, columns = ['id','views', 'price', 'space', 'rooms', 'latitude', 'longitude'])
    # print(dataDF)

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
    df = pd.DataFrame(principalComponents, columns = ['train_A','train_B','train_C'])
    testDf = pd.DataFrame(testPC, columns = ['test_A','test_B','test_C'])

    df.to_csv('train_data.csv', index = None)
    testDf.to_csv('test_data.csv', index = None)
    
    trainDf = pd.concat([df, dataDf[["price"]]], axis = 1)
    testDf2 = pd.concat([testDf, testDataDf[["price"]]], axis = 1)
    return trainDf, testDf2

def logReg(trainDf, testDf2):
    logisticRegr = LogisticRegression(solver = 'lbfgs')

    features = ['test_A','test_B','test_C']
    test_targets = testDf2.loc[:, ['price']].values
    test_feats = testDf2.loc[:, features].values
    test_feats = StandardScaler().fit_transform(test_feats)
    
    features = ['train_A', 'train_B', 'train_C']
    train_targets = trainDf.loc[:, ['price']].values
    train_feats = trainDf.loc[:, features].values
    train_feats = StandardScaler().fit_transform(train_feats)
    
    logisticRegr.fit(train_feats, train_targets)

    logisticRegr.predict(test_feats[0].reshape(1,-1))
    logisticRegr.score(test_feats, test_targets)

if __name__ == '__main__':
    trainDf, testDf2 = dimRed()
    logReg(trainDf, testDf2)
