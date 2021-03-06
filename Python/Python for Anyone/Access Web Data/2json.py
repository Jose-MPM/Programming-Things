import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

url = "UW Madison"

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
address = url
#input('Enter location: ')
#if len(address) < 1: break

parms = dict()
parms['address'] = url
    
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)


print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

print(json.dumps(js, indent=4))

print(js["results"][0]["place_id"])
