load("IF-MIB")
load("RFC1213-MIB")
load("SNMPv2-SMI")
load("SNMPv2-TC")
load("SNMPv2-CONF")
load("SNMPv2-MIB")
load("IANAifType-MIB")
load("/usr/share/mibs/cisco/CISCO-SMI.my")
load("SNMP-FRAMEWORK-MIB")
load("RMON-MIB")
load("/usr/share/mibs/cisco/CISCO-TC.my")
load("/usr/share/mibs/cisco/CISCO-VTP-MIB.my")
load("RFC1155-SMI")
load("RFC-1212")
#load("SNMPv2-TC-v1")
load("/usr/share/mibs/cisco/CISCO-CDP-MIB.my")

def hex2ip(hex):
    """
    Convert hex string to IPv4
    
    hex -- input string
    """
    res = ""
    dot = False
    for c in hex:
        if dot:
            res += "."
        else:
            dot = True
        res += str(ord(c))
    return res

m= M(host='172.30.101.11', community='RO')
for i in m.cdpCacheDevicePort:
    print m.ifDescr[i[0]],"-",m.cdpCacheDeviceId[i],m.cdpCacheDevicePort[i],m.cdpCachePlatform[i],hex2ip(m.cdpCacheAddress[i].__str__())

