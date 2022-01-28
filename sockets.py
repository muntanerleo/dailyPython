# here we will simiulate what will happen in a web browser
# with this small program we can get the contents of  website

import socket

# code below: makes the socket. this can be thought as a file handle that has no data associated with it yet.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# code below: reaches out and connects the socket to a destination, in this case (data.pr4e.org) and port 80. keep in mind that this could fail.
mysock.connect(('data.pr4e.org', 80))
# code below: now i send the http command. we add the .encode() at the end because there are strings inside python that are in unicode and i need to send them out in UTF-8. (if \n\n doesnt work, try \r\n\r\n).
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

# here i have a simple while loop that asks for up to 512 characters at a time. i will know if it is the end of file when the data recieved is less than 1. then the data will be printed. i need to use the .decode() because the data that i get back is UTF-8 encoded. .decode() turns it into the internal format called unicode.
while True:
  data = mysock.recv(512)
  if (len(data) < 1):
    break
  print(data.decode())
# code below: closes the connection
mysock.close()