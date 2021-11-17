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

    # pd.DataFrame(data, columns= ['id','views', 'price', 'space', 'rooms', 'latitude', 'longitude'])
    # cols = ['price', 'space', 'rooms']
    # Q1 = df[cols].quantile(0.25)
    # Q3 = df[cols].quantile(0.75)
    # IQR = Q3 - Q1
    # df = df[~((df[cols] < Q1 - 1.5 * IQR)) | (df[cols] > (Q3+ 1.5))]

    training_data, testing_data = train_test_split(data, test_size=0.2, random_state=25)

    dataDf = pd.DataFrame(training_data, columns = ['id','views', 'price', 'space', 'rooms', 'latitude', 'longitude'])
    testDataDf = pd.DataFrame(testing_data, columns = ['id','views', 'price', 'space', 'rooms', 'latitude', 'longitude'])

    features = ['views', 'space', 'rooms', 'latitude', 'longitude']
    feats = dataDf.loc[:, features].values
    feats = StandardScaler().fit_transform(feats)

    testFeats = testDataDf.loc[:, features].values
    testFeats = StandardScaler().fit_transform(testFeats)

    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(feats)
    testPC = pca.fit_transform(testFeats)
    
    print(np.cumsum(pca.explained_variance_ / np.sum(pca.explained_variance_))[0])

    df = pd.DataFrame(principalComponents, columns = ['train_A', 'train_B'])
    testDf = pd.DataFrame(testPC, columns = ['test_A', 'train_B'])

    df.to_csv('train_data.csv', index = None)
    testDf.to_csv('test_data.csv', index = None)
    
    trainDf = pd.concat([df, dataDf[["price"]]], axis = 1)
    testDf2 = pd.concat([testDf, testDataDf[["price"]]], axis = 1)
    return trainDf, testDf2