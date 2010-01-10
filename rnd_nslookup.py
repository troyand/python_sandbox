def get_random_IP_address():
    import ipaddr
    import random
    return str(ipaddr.IPAddress(random.randrange(0,4294967296)))

def get_hostname_by_addr(addr):
    import socket
    try:
        hostname, aliaslist, ipaddrlist = socket.gethostbyaddr(addr)
        print '[ok]',hostname
        return hostname
    except socket.herror:
        print '[no]',addr
        return ''

if __name__ == '__main__':

    #import doctest
    #doctest.testmod()

    import time
    print time.ctime()

    from multiprocessing import Pool
    pool = Pool(processes=50)

    ip_addresses = []
    for i in range(0,10):
        ip_addresses.append(get_random_IP_address())
    #import ipaddr
    #for ip in ipaddr.IPNetwork('194.44.142.0/23').iterhosts():
    #    ip_addresses.append(str(ip))

    hostnames = pool.map(get_hostname_by_addr, ip_addresses)

    for pair in zip(ip_addresses, hostnames):
        url, title = pair
        print url.ljust(18), '=> ', title

    print time.ctime()
