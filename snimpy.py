manager.load('CISCO-PRODUCTS-MIB')
manager.loaded
products_mib = manager.loaded[3]
product_nodes = mib.getNodes(products_mib)
for i in product_nodes:
    if i.oid == m.sysObjectID.value:
        print i

mib.getTables('IF-MIB')
ifTable = mib.getTables('IF-MIB')[0]
ifTable.index[0]
ifTable.columns
manager.ProxyColumn(m._session,ifTable.index[0])
print manager.ProxyColumn(m._session,ifTable.index[0]).proxy # ifIndex
proxies = []
for i in ifTable.columns:
    proxies.append(manager.ProxyColumn(m._session,i))

for j in proxies:
    print j.proxy,

print ''

for i in manager.ProxyColumn(m._session,ifTable.index[0]):
    for j in proxies:
        print j[i],
    print ''


def print_table(m,table):
    proxies = []
    for i in table.columns:
        proxies.append(manager.ProxyColumn(m._session,i))
    for j in proxies:
        print j.proxy,
    print ''
    for i in proxies[1]:
        for j in proxies:
            try:
                print j[i],
            except:
                pass
        print ''
    return None

