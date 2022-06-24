import json
import jsonschema
from jsonpath import jsonpath
from jsonschema import validate

with open('C:\\Users\\saravanan_s\\PycharmProjects\\pythonProject21\\comparejson1.json') as f1:
    data1 = json.load(f1)
with open('C:\\Users\\saravanan_s\\PycharmProjects\\pythonProject21\\comparejson1.json') as f2:
    data2 = json.load(f2)

    print(data1==data2)

print(jsonpath(data1,"client['name']"))
print(jsonpath(data1,"client1['name']"))

studentSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rollnumber": {"type": "number"},
        "marks": {"type": "number"},
    },
}

def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=studentSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
jsonData = json.loads('{"name": "jane doe", "rollnumber": "25", "marks": 72}')
# validate it
isValid = validateJson(jsonData)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")

# Convert json to python object.
jsonData = json.loads('{"name": "jane doe", "rollnumber": "af", "marks": 72}')
# validate it
isValid = validateJson(jsonData)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")