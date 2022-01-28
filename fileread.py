# write a program to read through a file and print the contontents of the file-
# (line-by-line) in all uppercase
 
# here i start by declaring the variable fhand that will open the file.
# then i print the contents in the file. remeber that i run it in the terminal.
# fhand = open('mbox-short.txt')

# to read the file i use the for loop
# what that will do is print out every line in the file
# i will use the .rstrip() to get rid of the white space and the .upper() to make it upper case
# for line in fhand:
  # lineY = line.rstrip()
  # print(lineY.upper())

hand = open('mbox-short.txt')

for line in hand:
  line = line.rstrip()
  words = line.split()
  
  # guardian pattern: if the word doesnt have 3 words, skip
  if len(words) < 3:
    continue
  if words[0] != 'From':
    continue
  print(words[2])