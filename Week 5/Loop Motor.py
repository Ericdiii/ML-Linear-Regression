# Insert needed package
import pandas as pd
import joblib

# Infinite loop
a = 1
while a < 10:
    # Insert data
    df = pd.read_csv("test_motor.csv", sep = ',')
    X = df.drop(['Status'], axis = 'columns')
    # Determine whether the csv file has NaN
    NaN = df.isnull().any()
    NV = NaN.values
    # Determine whether the csv file has been updated
    if True in NV:
        regr = joblib.load('Model_Motor.pkl')
        name_list = []
        to_list = regr.predict(X)
        print(to_list)
        for i in to_list:
            name_list.append(i)
        # Assign predicted value
        df["Status"] = name_list
        df.to_csv("test_motor.csv", encoding='utf')
    else:
        print('Waiting data')