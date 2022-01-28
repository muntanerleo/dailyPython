import urllib.request, urllib.parse, urllib.error
# this program does the same as the sockets one except that by using the urllib import, it cuts a lot of the code down.

# code below: create a handle and open the desired file
fhandler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# code below: reads line by line and decodes and strips
for line in fhandler:
  print(line.decode().strip())