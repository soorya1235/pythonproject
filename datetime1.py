# from datetime import datetime
# d1="25/04/01 02:35:5.22"
# formtdate="%d/%m/%y %H:%M:%S.%f"
# d2=datetime.strptime(d1,formtdate)
# print(d2.day)
# print(d2.year)
# print(d2.month)
# print(d2.minute)
# print(d2.second)
# print(d2.microsecond)

from datetime import datetime

# consider the time stamps from a list  in string
# format DD/MM/YY H:M:S.micros
time_data = ["28/05/99 02:35:8.023", "27/05/99 12:45:0.003",
             "26/05/99 07:35:5.523", "25/05/99 05:15:55.523"]

# format the string in the given format : day/month/year
# hours/minutes/seconds-micro seconds
format_data = "%d/%m/%y %H:%M:%S.%f"

# Using strptime with datetime we will format string
# into datetime
for i in time_data:
    print(datetime.strptime(i, format_data))
time_data.sort()
print(time_data)