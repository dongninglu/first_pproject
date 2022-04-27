'''
Created on Apr 16, 2022

@author: dongn
'''
from requests.auth import HTTPBasicAuth
import requests
import pprint
import json

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
disable_warnings(InsecureRequestWarning)


def my_delete_loopservices(services_name):
    my_endpoint = "https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service="
    for name in services_name :
        my_delete_endpoint = my_endpoint+name
        r = requests.delete(my_delete_endpoint,  auth=HTTPBasicAuth('admin','admin'), headers=my_headers,verify=False)
        print("----------------------delete -------------------------")
        print(r.url)
        pprint.pprint(r.status_code)
        pprint.pprint(r.headers["content-type"])



base_url = f"https://10.10.20.50:8888"
endpoint_path_data = f"/restconf/data"
endpoint_path_devices = f"{endpoint_path_data}/tailf-ncs:devices"
endpoint = f"{base_url}{endpoint_path_devices}/device"  


my_params = {'fields':'name'}
my_data = '{ "loopback-service:loopback-service": [ { "name": "test2", "device": "dist-rtr01", "dummy": "1.1.1.1"} ] }'
my_newname = "foobar"
my_headers = { 'Content-Type': 'application/yang-data+json;charset=utf-8'}

#
#get all devices names 
#and create a loopback service for each of them 
#
#device?fields=name
r = requests.get(endpoint,auth=HTTPBasicAuth('admin','admin'),headers=my_headers,params=my_params,verify=False )
"""
# get config info for edge-sw01
#r = requests.get(endpoint,auth=HTTPBasicAuth('admin','admin'),headers=my_headers )
# Create loopback-service
#r = requests.patch('http://10.10.20.50:8080/restconf/data/loopback-service:loopback-service', auth=HTTPBasicAuth('admin','admin'),headers=my_headers, data=data1)
# delete  loopback service
#r = requests.delete('http://10.10.20.50:8080/restconf/data/loopback-service:loopback-service=test2', auth=HTTPBasicAuth('admin','admin'),headers=my_headers)

print(r.url)

print(" see response code ...22222..........................")
pprint.pprint(r.status_code)
pprint.pprint(r.headers["content-type"])
print(" check data ...444..................................")

"""

if r.status_code in range(200, 299):
    data = r.json()
#    pprint.pprint(data)
    results = data['tailf-ncs:device']
    if len(results) > 0:
#        print("results[0].keys()--- 55555   ")
#        print(results[0].keys())
        i=0 
        m_servicename = []
        
        for result in results:
            
            device_name = result['name']
            print("  results[name]--- 66666   " +  result['name'] )
            my_updatedData = json.loads(my_data)
            my_value= my_updatedData['loopback-service:loopback-service']
            my_list= my_value[0];
            
            m_servicename.append(my_newname+str(i))
            
#            print ("---------------77777777777777777777700000000----------------")
#            pprint.pprint(m_servicename)
#            pprint.pprint(my_updatedData)
#            print ("original    "  )
            my_updatedData['loopback-service:loopback-service'][0].update({'device': device_name}) 
            my_updatedData['loopback-service:loopback-service'][0].update({'name': my_newname+str(i)})
            my_newdatastr = json.dumps(my_updatedData)

        
            r = requests.patch('https://10.10.20.50:8888/restconf/data/loopback-service:loopback-service', 
                               auth=HTTPBasicAuth('admin','admin'),headers=my_headers, data=my_newdatastr,verify=False)
            i = i+1

#            print (" updated   ------------00000000000000000000000000000----------- ")
#            print(r.url)
#            pprint.pprint(my_updatedData)
#            pprint.pprint(my_data)
#            print(" see response code ...001001001001001----------------------")
#            pprint.pprint(r.status_code)

        
        user_delete = input(" type any key to delete added loopservices .....")
        print ("deleting ....  ")
        my_delete_loopservices(m_servicename)
           

