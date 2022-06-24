from datetime import datetime

da=["25/12/01","25/11/01","25/10/01","25/09/01"]
da1="25/12/01"
fs="%y/%m/%d"
print(da)
da.sort()
print(da)

ss=datetime.strptime(da1,fs)
print(ss.day)
print(ss.month)
print(ss.year)

print(type(ss))
print(ss.date())