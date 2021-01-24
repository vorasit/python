import json
x = '{ "name": "pin" , "age" : "24"}'

y = json.loads(x)
print(y["name"])

a = { "name": "pin" , "age" : "24"}
z = json.dumps(a)
print(z)