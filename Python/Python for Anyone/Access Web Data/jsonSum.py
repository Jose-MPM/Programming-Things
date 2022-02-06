import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ")
#url = "https://py4e-data.dr-chuck.net/comments_42.json"
print("Retrieving", url)
controlador = urllib.request.urlopen(url)
data = controlador.read().decode()
info = json.loads(data)
print("Retrieving", len(data), "characters")
print(json.dumps(info, indent=4))
count = info["comments"]
#print(count)
sumTotal = 0
num = 0
for name  in count:
	num = name["count"]
	sumTotal += num
	num += 1

print("Count:", len(count))
print("Sum:", sumTotal)
