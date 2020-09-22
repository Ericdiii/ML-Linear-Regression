import datetime
from dateutil.relativedelta import relativedelta

# The date of parts start to be used
DS = '2020-6-1 09:30:05'
Date_Start = datetime.datetime.strptime(DS, '%Y-%m-%d %H:%M:%S')

# The longest days for use (State 3)
Date_Finish = Date_Start + relativedelta(days=365)

# The date now
DN = datetime.datetime.now()
Date_Now = datetime.datetime.strptime(DN.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')

# How long can this parts still work (Finish date subtract date of now)
e = Date_Finish-Date_Now
Lifecycle = format(e.days)

print(Date_Start)
print(Date_Now)
print(Date_Finish)
print(Lifecycle)
