fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

dictionary = dict()
for line in handle:
  line = line.rstrip()
  words = line.split()
  for word in words:
    # get allows us to get a value out if the key exists. default if its not there.
    # idiom: retrieve/create/update counter
    dictionary[word] = dictionary.get(word,0) + 1


# now we want to look for the most common word in the dictionary

# loop through the Key, Value pairs with the following syntax
for key,value in dictionary.items():
  print(key,value)