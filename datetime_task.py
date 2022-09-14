from datetime import datetime, date, timedelta
dt_today = datetime.now()
#today task
print("today is -", dt_today)

#yesterday task
yt_delta = timedelta(days=1)
yesterday = dt_today - yt_delta
print("yesterday was -", yesterday)

#month ago task
month_delta = timedelta(weeks=4)
month = dt_today - month_delta
print("a month ago was - ", month)

#turning str into an object datetime
date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
print("str in a datetime object - ", date_dt)
