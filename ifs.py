load("IF-MIB")
load("RFC1213-MIB")
m = M(host='172.30.101.11', community='RO')
for i in m.ifIndex:
    print m.ifIndex[i]," - ",m.ifDescr[i],m.ifAdminStatus[i],m.ifInOctets[i]

