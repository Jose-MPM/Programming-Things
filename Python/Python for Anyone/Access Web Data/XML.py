import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
file = """<commentinfo>
<note>
This file contains the actual data for your assignment - good luck!
</note>
<comments>
<comment>
<name>Jenson</name>
<count>100</count>
</comment>
<comment>
<name>Afifah</name>
<count>99</count>
</comment>
<comment>
<name>Tobey</name>
<count>98</count>
</comment>
<comment>
<name>Emma</name>
<count>97</count>
</comment>
<comment>
<name>Billiejo</name>
<count>97</count>
</comment>
<comment>
<name>Zane</name>
<count>95</count>
</comment>
<comment>
<name>Indy</name>
<count>95</count>
</comment>
<comment>
<name>Seatle</name>
<count>92</count>
</comment>
<comment>
<name>Kynan</name>
<count>92</count>
</comment>
<comment>
<name>Zain</name>
<count>89</count>
</comment>
<comment>
<name>Bronwen</name>
<count>88</count>
</comment>
<comment>
<name>Elora</name>
<count>85</count>
</comment>
<comment>
<name>Kainin</name>
<count>83</count>
</comment>
<comment>
<name>Bartosz</name>
<count>82</count>
</comment>
<comment>
<name>Vanya</name>
<count>82</count>
</comment>
<comment>
<name>Hiro</name>
<count>78</count>
</comment>
<comment>
<name>Cleo</name>
<count>76</count>
</comment>
<comment>
<name>Taisha</name>
<count>76</count>
</comment>
<comment>
<name>Wendy</name>
<count>75</count>
</comment>
<comment>
<name>Adrianna</name>
<count>71</count>
</comment>
<comment>
<name>Haniya</name>
<count>70</count>
</comment>
<comment>
<name>Adele</name>
<count>69</count>
</comment>
<comment>
<name>Alannah</name>
<count>64</count>
</comment>
<comment>
<name>Limbiadhe</name>
<count>62</count>
</comment>
<comment>
<name>William</name>
<count>61</count>
</comment>
<comment>
<name>Saad</name>
<count>56</count>
</comment>
<comment>
<name>Rai</name>
<count>54</count>
</comment>
<comment>
<name>Mahmoud</name>
<count>52</count>
</comment>
<comment>
<name>Erina</name>
<count>51</count>
</comment>
<comment>
<name>Brookelyn</name>
<count>47</count>
</comment>
<comment>
<name>Rhyley</name>
<count>40</count>
</comment>
<comment>
<name>Tobias</name>
<count>39</count>
</comment>
<comment>
<name>Alvin</name>
<count>38</count>
</comment>
<comment>
<name>Janel</name>
<count>36</count>
</comment>
<comment>
<name>Tiarnan</name>
<count>33</count>
</comment>
<comment>
<name>Melisa</name>
<count>32</count>
</comment>
<comment>
<name>Ronnie</name>
<count>31</count>
</comment>
<comment>
<name>Walid</name>
<count>30</count>
</comment>
<comment>
<name>Danelle</name>
<count>27</count>
</comment>
<comment>
<name>Abel</name>
<count>24</count>
</comment>
<comment>
<name>Woyenbrakemi</name>
<count>20</count>
</comment>
<comment>
<name>Nico</name>
<count>17</count>
</comment>
<comment>
<name>Atiya</name>
<count>16</count>
</comment>
<comment>
<name>Pushkar</name>
<count>14</count>
</comment>
<comment>
<name>Arshita</name>
<count>11</count>
</comment>
<comment>
<name>Joshua</name>
<count>11</count>
</comment>
<comment>
<name>Saicu</name>
<count>8</count>
</comment>
<comment>
<name>Eila</name>
<count>7</count>
</comment>
<comment>
<name>Riach</name>
<count>5</count>
</comment>
<comment>
<name>Katherine</name>
<count>3</count>
</comment>
</comments>
</commentinfo>"""
while True:
    tree = ET.fromstring(file)
    suma = 0
    results = tree.findall("comments/comment")
    for item in results:
        x = item.find("count").text
        print(x)
        num = int(x)
        suma = suma + num
    print("Sum: ", suma)
    break

