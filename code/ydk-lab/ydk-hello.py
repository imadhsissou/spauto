# import providers, services and models
from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xr import Cisco_IOS_XR_shellutil_oper \
    as xr_shellutil_oper
from datetime import timedelta


if __name__ == "__main__":
    """Main execution path"""

    # create NETCONF session
    provider = NetconfServiceProvider(address="sbx-iosxr-mgmt.cisco.com",
                                      port=10000,
                                      username="admin",
                                      password="C1sco12345",
                                      protocol="ssh")
    # create CRUD service
    crud = CRUDService()

    # create system time object
    system_time = xr_shellutil_oper.SystemTime()

    # read system time from device
    system_time = crud.read(provider, system_time)

    # print system uptime
    print("System uptime is " +
          str(timedelta(seconds=system_time.uptime.uptime)))

    exit()