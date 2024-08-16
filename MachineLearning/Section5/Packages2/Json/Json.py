import json
data = {'name' : 'Jayesh', 'age' : '21'}
data = json.dumps(data)
print(data)
print(type(data))
data = json.loads(data)
print(data)
print(type(data))
