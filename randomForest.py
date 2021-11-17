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

    dataDf = pd.DataFrame(training_data, columns = ['id','views', 'price', 'space', 'rooms', 'latitude', 'longitude'])
    testDataDf = pd.DataFrame(testing_data, columns = ['id','views', 'price', 'space', 'rooms', 'latitude', 'longitude'])

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
