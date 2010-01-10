#!/usr/bin/snimpy

load("IP-FORWARD-MIB")
m = M(host='172.30.101.11', community='RO')

routes = m.ipCidrRouteNextHop
for x in routes:
    net, netmask, tos, src = x
    print routes[x],repr(routes[x])
    print "%15s/%-15s via %-15s src %-15s" % (net, netmask, routes[x], src)
