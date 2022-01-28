# create a list of the most common words and find out how to sort a dictionary by the value, instead of by the key.

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

# make an empty dictionary
dictionary = dict()
for line in handle:
  line = line.rstrip()
  # 'words' splits the lines into words
  words = line.split()
  # the for loop goes through the words and makes the counters using the idiom
  for word in words:
    # idiom: retrieve/create/update counter
    dictionary[word] = dictionary.get(word,0) + 1

# print(dictionary)

# now we hand contruct a list 
temp = list()
for key,value in dictionary.items():
  # make a new tuple
  newTuple = (value,key)
  # now by appending, i end up with a list of tuples
  temp.append(newTuple)

# print('Flipped',temp)

# now take temp, sort it, and give it back to me
temp = sorted(temp, reverse=True)
# print('Sorted',temp)

# loop to flip then back to key and value
for value,key in temp[:5] :
  print(key,value)