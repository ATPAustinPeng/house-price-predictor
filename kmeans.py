import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px
import matplotlib.pyplot as plt


df = pd.read_csv('clean_data.csv')
df = df.iloc[:,2:4]
print(df)
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

km1 = KMeans(n_clusters=3, random_state=42).fit(df) #Assigning clusters based of just looking at the data
clusters1 = pd.DataFrame(km1.labels_, columns=['cluster'])
df1 = pd.concat([df, clusters1], axis=1)
fig1 = px.scatter(df1, df.iloc[:,0],df.iloc[:,1], color = 'cluster') #Creating cluster scatterplot
fig1.show() # Error handling- using different figures to create seperate windows easierw
