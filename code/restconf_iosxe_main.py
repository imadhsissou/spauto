import sys
import yaml
from restconf_iosxe_classes import TemplateXe, RequestXe, InterfaceXe, AutomateXe


credentials = open("credentials.yml", "r")
interfaces = open("interfaces.yml", "r")

template = TemplateXe()
request = RequestXe(yaml.load(credentials, Loader=yaml.FullLoader)[0])
intf = InterfaceXe(yaml.load(interfaces, Loader=yaml.FullLoader)[0])
instance = AutomateXe()


def create(inst):
    inst.autoCreate(template, request, intf)


def read(inst):
    inst.autoRead(template, request, intf)


def delete(inst):
    inst.autoDelete(template, request, intf)


def autoInstance(crud):
    globals()[crud](instance)


if __name__ == "__main__":
    autoInstance(sys.argv[1])
