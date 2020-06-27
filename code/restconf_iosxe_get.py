import requests
import json
from pprint import pprint

url = 'https://ios-xe-mgmt.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/vrf/definition="VRF_DEF_USING_RESTCONF"'

headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

PythonObjectResponse = requests.get(url, headers=headers, verify=False)

PythonObjectResponse = PythonObjectResponse.json()
#PythonObjectResponse = json.loads(PythonObjectResponse.text)

JSONResponse = json.dumps(PythonObjectResponse, indent=2, sort_keys=False)

print(JSONResponse)