from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
import csv



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

dataDf = pd.DataFrame(data, columns = ['price','space', 'rooms', 'bedrooms', 'furniture', 'latitude', 'longitude'])
features = ['space', 'rooms', 'bedrooms', 'furniture', 'latitude', 'longitude']
feats = dataDf.loc[:, features].values
feats = StandardScaler().fit_transform(feats)
norm1 = feats / np.linalg.norm(feats)
price = dataDf['price']

model = Pipeline([('poly', PolynomialFeatures(degree=3)), ('ridge', Ridge(fit_intercept=False))])
model = model.fit(feats, price)
print(model.score(feats, price))

n_samples, n_features = 10, 5
rng = np.random.RandomState(0)
clf = Ridge(alpha=5)
clf2 = Lasso(alpha=1.0)
clf.fit(feats, price)
clf2.fit(feats, price)
print(clf.score(feats, price))
print(clf2.score(feats, price))