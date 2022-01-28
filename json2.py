import json

input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

# code below: parses the json and converts it into a python list, (it is a list because the json has []) 
info = json.loads(input)
print('User count:', len(info))

# code below: parses through the json taking in the id, x, name and turns them into arrays.
for item in info:
  print('Name', item['name'])
  print('Id', item['id'])
  print('Attributes', item['x'])