import urllib.request, urllib.parse, urllib.error
import json

# program using google api to retrieve a page and tare it apart

# Note: google is increasingly requiring keys for this API

# code below: gets the url needed
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# code below: while loop that runs and asks for the location.
while True:
  address = input('Enter location: ')
  if len(address) < 1: break

  # code below: concatinate the service url and urllib.parse.urlencode
  url = serviceurl + urllib.parse.urlencode({'address': address})

  print('Retrieving', url)
  # code below: url open to get the handle 
  uhandle = urllib.request.urlopen(url)
  # read the whole document and decode content
  data = uhandle.read().decode()
  # code below: prints out the data collected and how many characters i got.
  print('Retrieved', len(data), 'characters')

  # load the json content. using a try and except just in-case it blows up
  try:
    js = json.loads(data)
  except:
    js = None

  # code below: debugging if statement in case i get a false, if i dont have a status key in the js object/dictionary.
  if not js or 'status' not in js or js['status'] != 'OK':
    print('==== FAILURE TO RETRIEVE ====')
    print(data)
    continue

  # code below: call json dumps, which has the dictionary that includes arrays and pretty print it with an indent of 4.
  print(json.dumps(js, indent=4))

  lat = js["results"][0]["geometry"]["location"]["lat"]
  lng = js["results"][0]["geometry"]["location"]["lng"]
  print('lat', lat, 'lng', lng)
  location = js['results'][0]['formatted_address']
  print(location)