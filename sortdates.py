from datetime import datetime
from datetime import date
# my_dates = ['5-Nov-18', '25-Mar-17', '1-Nov-18', '7-Mar-17']
# #my_dates = ['5-11-18', '25-0317', '1-11-18', '7-03-17']
# my_dates.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))
# print(my_dates)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

def myFunc(e):
  return len(e)

cars1 = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars1.sort(reverse=False, key=myFunc)
print(cars1)