import jsonschema
from jsonschema import validate
import json
scheme = {
    "type" : "object",
    "properties" :
      {
       "name" : {"type" : "string"}
      }
}

str='{"name" :1}'
str1=json.loads(str)
def val(str1,scheme):
    try:
        validate(str1,scheme)
        return True
    except jsonschema.exceptions.ValidationError as err:
       print("json schema is invalid")
       return False

print(val(str1,scheme))