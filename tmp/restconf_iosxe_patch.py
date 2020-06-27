import requests
import json

url = "https://ios-xe-mgmt.cisco.com:9443/restconf/data/Cisco-IOS-XE-native:native/vrf/definition/"

payload = {
	   "definition":[
      {
         "name":"VRF_DEF_USING_RESTCONF",
         "rd":"67710:100",
         "address-family":{
            "ipv4":{
               "route-target":{
                  "export":[
                     {
                        "asn-ip":"67710:101"
                     }
                  ],
                  "import":[
                     {
                        "asn-ip":"67710:102"
                     }
                  ]
               }
            }
         }
      }
   ]
}

JSONpayload = json.dumps(payload)

headers = {
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

PythonObjectResponse = requests.patch(url, headers=headers, data = JSONpayload, verify=False)

print(PythonObjectResponse)