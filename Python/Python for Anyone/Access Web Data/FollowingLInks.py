# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ultimo = ""

def find(Link, posi, number):
	if(number != 0):
		# Ignore SSL certificate errors
		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE

		url = Link
		html = urllib.request.urlopen(url, context=ctx).read()
		soup = BeautifulSoup(html, 'html.parser')

		# Retrieve all of the anchor tags
		tags = soup('a')
		pos = posi
		for tag in tags:
			x = tag.get("href", None)
			pos = pos - 1
			#print(str(x))
			if pos < 0:
				break
			elif (pos == 0):
				y = tag.get("href", None)
				print("Retrieving: ",y)
				find(str(y), posi, number-1)
				break
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))
find(url, position, count)