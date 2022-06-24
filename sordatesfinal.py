from datetime import datetime
my_dates = ['5-Nov-18', '25-Mar-17', '1-Nov-18', '7-Mar-17']
two_dates = ['15-Jan-18', '14-Jan-18', '13-Jan-18', '7-Jan-18']
my_dates.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))
print(my_dates)


two_dates.sort(key=lambda date : datetime.strptime(date,"%d-%b-%y"))
print(two_dates)



x=lambda x : x**2
print(x(2))

x=lambda x : True if x%2==0 else False
print(x(10))

lst1=[1,2,3,4,4,5,6,6,7,77,8,9,9,33,4,4,5,6]
print(list(filter(lambda x: x%2==0,lst1)))

lst1 = [x for x in range(1,100) if x%2==0]
print(lst1)

mp1=[1,2,3,4,5,6]
mp1=map(lambda x:x*x,mp1)
print(list(mp1))

mp2=[1,2,3,4,4,5,6,7,9]
from functools import reduce
abc=reduce(lambda x,y:x+y,mp2)
print(abc)