import requests

url = httpsapi.hubapi.comcrmv3objectscontacts

querystring = {limit20,propertiesemail,firstname,after121}

payload = 
headers = {Authorization Bearer pat-na1-5ff98a29-f5d0-4378-a930-5a939760419f}

response = requests.request(GET, url, data=payload, headers=headers, params=querystring)

print(response.text)