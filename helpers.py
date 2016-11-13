#!/usr/bin/python

import netifaces


def get_interfaces(type):
    interfaces = netifaces.interfaces()
    if len(interfaces) >= 0:
        if type == "single":
            gws = netifaces.gateways()
            gateway = (gws['default'][netifaces.AF_INET][1:2])
            interfaces = str(gateway).strip('()\',')
            return(interfaces)
        else:
            return(str(interfaces))
    else:
        return("No interfaces")


def get_gateway():
    gws = netifaces.gateways()
    gateway = (gws['default'][netifaces.AF_INET][:1])
    gateway = str(gateway).strip('()\',')
    return(gateway)
