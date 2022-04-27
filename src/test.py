'''
Created on Apr 16, 2022

@author: dongn
'''

from requests.auth import HTTPBasicAuth
import requests
import pprint
import json
from certifi_win32.wincerts import verify_combined_pem

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)

# HTTP request METHODS
"""
GET -> grab data
POST -> add/update data
PATCH
PUT
DELETE
"""

# what's our endpoint (or a url)?

# what is the HTTP method that we need?


my_data = '{ "loopback-service:loopback-service": [ { "name": "test4", "device": "dist-rtr01", "dummy": "1.1.1.1"} ] }'


my_string = "newhost"

print("my_data type is  ..... " ) 
print( type(my_data))

  

my_original = json.loads(my_data)
my_jsonstring= json.dumps(my_original)

if my_data == my_jsonstring :
    print(" @@@@@@@@@@@@@@@@EQUAL@@@@@@@@@@")
else :
    print (my_data)
    print(my_original)
    print(my_jsonstring)

print(type(my_original))

pprint.pprint(my_original)
print ("original--------------111111111111111-----------------    "  )

print(type(my_original))

pprint.pprint(my_original)
my_original['loopback-service:loopback-service'][0].update({'name': my_string}) 
print (" updated2222222222---------------------22222222222222222-----------    ")
print(type(my_original))

pprint.pprint(my_original)
my_jsonstring= json.dumps(my_original)


my_headers = { 'Content-Type': 'application/yang-data+json;charset=utf-8'}

#requests.packages.urllib3.disable_warnings()
r = requests.get('https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service',
                 auth=HTTPBasicAuth('admin','admin'),
                 headers=my_headers,verify=False )
"""
r = requests.patch('https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service', 
                   auth=HTTPBasicAuth('admin','admin'),
                   headers=my_headers, 
                   data=my_jsonstring)
"""

print(" see response code ...22222")
pprint.pprint(r.status_code)

print(" see response content type ...333")
pprint.pprint(r.headers["content-type"])

pprint.pprint(r.json())


        #movie_ids.add(_id)


    
