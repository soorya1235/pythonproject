import os
import json
import re
from jsonpath import jsonpath
with open("C:\\Users\\saravanan_s\\PycharmProjects\\pythonProject21\\sample.json") as fs:
    s=json.load(fs)

print(s)
print(s['marks']['eng'])

# print(type(s))
# eng=jsonpath(s,"marks")
# print(eng)
# print(eng[0]['eng'])

s="10.10.10.10"
ls = re.split(r'\.',s)
print(ls)