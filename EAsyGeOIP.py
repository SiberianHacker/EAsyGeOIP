import os
import requests

ip = input("Enter IP: ")
req = requests.get("http://ip-api.com/json/" + ip)
content = req.text

if "fail" in content:
    print("Ip not working!")
    exit()
    os.system("pause")
    
country = content.split('country":"')[1].split('"')[0]
countryCode = content.split('countryCode":"')[1].split('"')[0]
city = content.split('city":"')[1].split('"')[0]
region = content.split('regionName":"')[1].split('"')[0]
regionCode = content.split('region":"')[1].split('"')[0]
zip_code = content.split('zip":"')[1].split('"')[0]
timezone = content.split('timezone":"')[1].split('"')[0]
isp = content.split('isp":"')[1].split('"')[0]
organization = content.split('org":"')[1].split('"')[0]
asn = content.split('as":"')[1].split('"')[0]

print("Country: " + country)
print("Country Code: " + countryCode)
print("City: " + city)
print("Region: " + region)
print("RG code: " + regionCode)
print("Zip code: " + zip_code)
print("Timezone: " + timezone)
print("ISP: " + isp)
print("Org. :" + organization)
print("ASN: " + asn)
os.system("pause")