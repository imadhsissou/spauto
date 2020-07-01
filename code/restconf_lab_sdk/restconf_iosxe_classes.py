import sys
import json
import requests
from collections import OrderedDict
from jinja2 import FileSystemLoader, Environment
from requests.packages.urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

loader = FileSystemLoader(["."])
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)


class TemplateXe:
    def createInterface(self, intf):
        rest_uri = "Cisco-IOS-XE-native:native/interface/Loopback"
        data = env.get_template("interfaces.j2").render(intf=intf)
        return rest_uri, data

    def readInterface(self, name):
        rest_uri = f"Cisco-IOS-XE-native:native/interface/Loopback={name}"
        data = ""
        return rest_uri, data

    def deleteInterface(self, name):
        rest_uri = f"Cisco-IOS-XE-native:native/interface/Loopback={name}"
        data = ""
        return rest_uri, data


class RequestXe:
    def __init__(self, creds):
        self.host = creds["host"]
        self.port = creds["port"]
        self.user = creds["user"]
        self.passwd = creds["passwd"]
        self.url = f"https://{self.host}:{self.port}/restconf/data/"
        self.headers = {
            "Content-Type": "application/yang-data+json",
            "Accept": "application/yang-data+json",
        }

    def createRequest(self, TemplateXeObj):
        url = self.url + TemplateXeObj[0]
        try:
            response = requests.patch(
                url,
                auth=(self.user, self.passwd),
                headers=self.headers,
                data=TemplateXeObj[1],
                verify=False,
            )
            print(f"Create Operation Status : {str(response.status_code)}")
        except:
            print(f"createRequest() : {str(sys.exc_info())}")
            print(f"Create Operation Status : {str(response.status_code)}")
            return 1

    def readRequest(self, TemplateXeObj):
        url = self.url + TemplateXeObj[0]
        try:
            response = requests.get(
                url,
                auth=(self.user, self.passwd),
                headers=self.headers,
                data=TemplateXeObj[1],
                verify=False,
            )
        except:
            print(f"readRequest() : {str(sys.exc_info())}")
            return 1
        if response.status_code == 200:
            response = json.loads(response.text, object_pairs_hook=OrderedDict)
            responseJSON = json.dumps(response, indent=2)
            print(f"Read Operation Status : 200 OK\n {responseJSON}")
        else:
            print(f"Read Operation Status : {str(response.status_code)}")

    def deleteRequest(self, TemplateXeObj):
        url = self.url + TemplateXeObj[0]
        try:
            response = requests.delete(
                url,
                auth=(self.user, self.passwd),
                headers=self.headers,
                data=TemplateXeObj[1],
                verify=False,
            )
            print(f"Delete Operation Status : {str(response.status_code)}")
        except:
            print(f"deleteRequest() : {str(sys.exc_info())}")
            print(f"Delete Operation Status : {str(response.status_code)}")
            return 1


class InterfaceXe:
    def __init__(self, intf):
        self.intf = intf
        self.name = intf["name"]
        self.description = intf["description"]
        self.address = intf["address"]
        self.mask = intf["mask"]


class AutomateXe:
    def autoCreate(self, TemplateXeObj, RequestXeObj, InterfaceXeObj):
        intfObj = TemplateXeObj.createInterface(InterfaceXeObj.intf)
        RequestXeObj.createRequest(intfObj)

    def autoRead(self, TemplateXeObj, RequestXeObj, InterfaceXeObj):
        intfObj = TemplateXeObj.readInterface(InterfaceXeObj.name)
        RequestXeObj.readRequest(intfObj)

    def autoDelete(self, TemplateXeObj, RequestXeObj, InterfaceXeObj):
        intfObj = TemplateXeObj.deleteInterface(InterfaceXeObj.name)
        RequestXeObj.deleteRequest(intfObj)
