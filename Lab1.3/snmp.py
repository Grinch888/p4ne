#!/usr/local/bin/python3

from pysnmp.hlapi import *

communty = "public"
ip = "10.31.70.107"
snmp = "SNMPv2-MIB/ sysDescr"
mib = "1.3.6.1.2.1.2.2.1.2"
snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

result = getCmd(SnmpEngine(),
                CommunityData(communty),
                UdpTransportTarget((ip, 161)),
                ContextData(),
                ObjectType(snmp_object))

for i in result:
    for j in i[3]:
        print(j)

snmp_object = ObjectIdentity(mib)
result2 = nextCmd(SnmpEngine(),
                  CommunityData(communty),
                  UdpTransportTarget((ip, 161)),
                  ContextData(),
                  ObjectType(snmp_object),
                  lexicographicMode=False)

for i in result2:
    for j in i[3]:
        print(j)





