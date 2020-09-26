# Insert needed package
import pandas as pd
import joblib
import datetime
from dateutil.relativedelta import relativedelta
import time

# The date of parts start to be used
DS = '2020-6-1'
Date_Start = datetime.datetime.strptime(DS, '%Y-%m-%d')

# The date now
DN = datetime.datetime.now()
Date_Now = datetime.datetime.strptime(DN.strftime('%Y-%m-%d'), '%Y-%m-%d')

# Longest days for use(LED)
Date_Finish1 = Date_Start + relativedelta(days=2083)

# Remain days for use (Best status)
Remain_days = Date_Finish1 - Date_Now
Days = format(Remain_days.days)
k = int(Days)
# Predict the lifecycle for healthy status
life3 = round(k)
Status_1and5 = k * 0.05
# Predict the lifecycle for bad status
life15 = round(Status_1and5)
Status_2and4 = k * 0.1
# Predict the lifecycle for poor status
life24 = round(Status_2and4)

Date_Finish_Status3 = Date_Now + relativedelta(days=k)
date_str_3 = Date_Finish_Status3.strftime('%Y-%m-%d')

# Remain days for use (Status 1&5)

Date_Finish_Status15 = Date_Now + relativedelta(days=Status_1and5)
date_str_15 = Date_Finish_Status15.strftime('%Y-%m-%d')

# Remain days for use (Status 2&4)

Date_Finish_Status24 = Date_Now + relativedelta(days=Status_2and4)
date_str_24 = Date_Finish_Status24.strftime('%Y-%m-%d')

# Infinite loop
a = 1
while a < 2:

    # Insert data
    df = pd.read_csv("current_LED.csv", sep=',')
    X = df.drop(['Status', 'Lifecycle', 'Predicted date'], axis='columns')

    # Determine whether the csv file has NaN
    NaN = df.isnull().any()
    NV = NaN.values

    # Determine whether the csv file has been updated
    if True in NV:
        regression = joblib.load('Model_LED.pkl')
        status_value = regression.predict(X)
        print(status_value)

        if 0 < status_value <= 1:
            df["Status"] = 'Bad'
            df["Lifecycle"] = life15
            df["Predicted date"] = date_str_15
            df.to_csv("current_LED.csv", encoding='utf')
        elif 1 < status_value <= 2:
            df["Status"] = 'Poor'
            df["Lifecycle"] = life24
            df["Predicted date"] = date_str_24
            df.to_csv("current_LED.csv", encoding='utf')
        elif 2 < status_value <= 3:
            df["Status"] = 'Healthy'
            df["Lifecycle"] = life3
            df["Predicted date"] = date_str_3
            df.to_csv("current_LED.csv", encoding='utf')
        elif 3 < status_value <= 4:
            df["Status"] = 'Poor'
            df["Lifecycle"] = life24
            df["Predicted date"] = date_str_24
            df.to_csv("current_LED.csv", encoding='utf')
        else:
            df["Status"] = 'Bad'
            df["Lifecycle"] = life15
            df["Predicted date"] = date_str_15
            df.to_csv("current_LED.csv", encoding='utf')

        ###############################################
        # Upload into server and show data in web page#
        ###############################################

    else:
        # Delay 5 seconds
        time.sleep(5)
