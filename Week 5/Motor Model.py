# Insert needed package
import pandas as pd
import numpy as np

# Insert dataset
import os
print (os.path.abspath('.'))
data_file = pd.read_csv('Dataset_Motor.csv')
df = pd.read_csv("Dataset_Motor.csv")

# Take a look at the dataset
df.head()
# Summarize the data
df.describe()
cdf = df[['Current','Status']]
cdf.head(9)
viz = cdf[['Current','Status']]
viz.hist()

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

# Simple linear regression model

from sklearn import linear_model
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['Current']])
train_y = np.asanyarray(train[['Status']])
regr.fit (train_x, train_y)

# Save the model
import joblib
joblib.dump(regr, 'Model_Motor.pkl')