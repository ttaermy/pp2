#1
import datetime

x = datetime.datetime.now()
new_date = x - datetime.timedelta(days=5)

print(new_date.date())

#2
import datetime

x = datetime.datetime.now()
yest = x - datetime.timedelta(days=1)
tmrw = x + datetime.timedelta(days=1)

print(yest.date())
print(x.date())
print(tmrw.date())

#3
import datetime

x = datetime.datetime.now()
wo = x.replace(microsecond=0)

print(wo)

#4
import datetime

date1 = datetime.datetime.now()
date2 = datetime.datetime(2025, 2, 16, 11, 55, 00)

diff = date2 - date1

insec = diff.total_seconds()
print(insec)