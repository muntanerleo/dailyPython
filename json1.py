import json

# in this program i will sort through a json file

# code below: here i just have the info for the json in a triple quoetes. (since it is in curly braces it will return a dictionary with key,value pairs)
data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
  },
  "email" : {
    "hide" : "yes"
  }
}'''

# code below: go into the json library and load string. parse the above json into a structered object. if there is a syntax error then it blows up. if it doesnt blow up then we hve a structured representation 
info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])