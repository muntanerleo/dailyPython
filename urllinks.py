import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# for this program to work you will need to have pip installed BeautifulSoup4

# ignore SSL certificate errors (helps with the HTTPS sites)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# code below: ask for the url
url = input('Enter - ')
# code below: gets all the html. return the entire document of the webpage in a single big string with new lines.
html = urllib.request.urlopen(url, context=ctx).read()
# code below: what the line is saying we are giving you nasty html that makes no sense, please read it and give us an object (soup). soup object is now clean!
soup = BeautifulSoup(html, 'html.parser')

# Retrive all the anchor tags 
tags = soup('a')
# loop through all the <a tags in the html and gives me back the href.
for tag in tags:
  print(tag.get('href', None))