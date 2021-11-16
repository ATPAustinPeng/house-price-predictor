# CS4641 Project Proposal: House Price Predictor

## Team Members

- Meena Ajith
- Srajan Sunil Dube
- Roshen Jegajeevan
- Nilesh Manivannan
- Austin Peng

## Introduction/Background

Various factors affect the prices of houses in any location. Without a proper way to determine the effect of those factors, it is impossible to find out the best time to purchase a house, which is obviously at the lowest value possible within a specific time frame. Many studies analyzed housing factors and long-term changes. However, these studies have been completed mainly in the US and Europe, examining developed countries in a capitalistic economy. Our project will aim to analyze the housing market of an untapped area such as Georgia (the country, not the state). Georgia ranks 100th in GDP per capita and is a developing country, but still has one of the most capitalistic societies in the world. Looking at the housing market in this country would allow us to gain new information that we couldn’t attain by doing the same repetitive analysis on Western countries. This machine learning analysis would yield both better predictive capability and detailed insight into a potentially untapped market.

## Problem Definition

What factors affect the housing market in Georgia and how could the economic, locational, and political environment forecast for the current and future housing market for certain areas?

## Data Collection

We performed the data collection through an analysis of different Eastern countries and their housing markets. We decided on Georgia after finding a housing dataset on Kaggle that had all the features we wanted to analyze. We assessed further datasets from other sources such as DataWorld, Redfin, and Zillow but decided to proceed further with Kaggle as there weren't significant amounts of housing information on Georgia.

## Methods

After attaining our dataset, we first cleaned up any errors, null values, and discrepancies. We first dropped any rows with any large amounts of null values. We then proceeded to drop any unnecessary columns that wouldn’t give us any useful information when we do our analysis. We checked for any errors such as housing prices being 0 or negative and then standardized the data to bring it into a uniform format. First, we proceeded with PCA and used dimensionality reduction to keep essential data and speed up calculations in the testing phase of the analysis. After dimensionality reduction, we decided to use logistic regression to find the correlation between different features in the housing market of Georgia. This is because logistic regression can be used to analyze the effects that each feature has on another. We decided to proceed with logistic regression over linear regression as we preferred to have a discrete result (the predicted price of the house) rather than a continuous result that we would get from linear regression. We utilized an 80/20 split when splitting out data up into training and testing components: 80% training and 20% testing. We performed logistic regression on the training data to create a model that would predict housing prices given certain features. We will then use this model with our testing data to test our final 20% to confirm the effectiveness and accuracy of our analysis.

## Potential Results And Discussion

There could be multiple interesting results that arise when we combine both long-term and short-term factors. For example, predictions that the housing market would crash during Covid were proven wrong when results arose that housing prices were resilient to pandemics (Grybauskas, Pilinkiene, Stundziene). Combining anomalies like this into our analysis would allow us to have a more effective model. We believe the results will be unexpected since the current time period is unique, given that we are not necessarily post-pandemic but businesses are still returning to normal with the economy's highest inflation rates since The Great Depression.

## Timeline

**October**
10/03 ~ 10/09

- Brainstorm and select a topic for the project.
- Do background research and create a timeline for the project.
- Complete project proposal.

10/10 ~ 10/16

- Find data to use and analyze for the model.

10/17 ~ 10/23

- Clean the data and build the dataset.

10/24 ~ 10/30

- Research and decide on the machine learning models to use for the project.



**November**
10/31 ~ 11/06

- Experiment with multiple approaches and incrementally increase	the number of features.

11/07 ~ 11/13

- Continue experimentation and adding features.

11/14 ~ 11/20

- Complete and submit midterm report.

11/21 ~ 11/27

- Test the model and calculate metrics for the model.

**December**

11/28 ~ 12/04

- Begin and complete rough draft of the final report.

12/05 ~ 12/07

- Make last-minute edits to the final report.



## References

Droes, Martijn, and Alex Van de Minne. “Do the Determinants of House Prices Change over Time? Evidence from 200 Years of Transactions Data.” *25th Annual European Real Estate Society Conference*, 2016, https://doi.org/10.15396/eres2016_227.

Grybauskas, Andrius, et al. “Predictive Analytics Using Big Data for the Real Estate Market during the COVID-19 Pandemic.” *Journal of Big Data*, vol. 8, no. 1, 2021, https://doi.org/10.1186/s40537-021-00476-0.

Ho, Winky K.O., et al. “Predicting Property Prices with Machine Learning Algorithms.” *Journal of Property Research*, vol. 38, no. 1, 2020, pp. 48–70., https://doi.org/10.1080/09599916.2020.1832558.

Kahn, James A. “What Drives Housing Prices?” *SSRN Electronic Journal*, 2008, https://doi.org/10.2139/ssrn.1264048. 
