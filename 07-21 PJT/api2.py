import json

json_data = '''
{
    "name" : "유형민",
    "age" : 30
}
'''
data = json.loads(json_data)
name = data.get('name')

print(data)
print(name)