def iter_t(indices,trees):
    """
    subtree -- 
    """
    for i in indices:
        print indices[i],
        for j in trees:
            print j[i],
        print ''

def tln():
    def cbcl(c,s):
        for i in s:
            c.send(i)
            c.expect_exact(i)
        c.sendline('')
    #
    child = pexpect.spawn('telnet 172.30.101.14')
    child.logfile_read = sys.stdout
    try:
        child.expect('assword:')
        child.sendline('c')
        child.expect('>')
        cbcl(child,'en')
        child.expect('assword:')
        child.sendline('c')
        child.expect('#')
        cbcl(child,'ping 172.30.101.1 size 1500 repeat 20 df-bit')
        child.expect('#')
        cbcl(child,'conf t')
        child.expect('#')
        cbcl(child,'snmp-server location $ ^ " m. Kyjiv, Central\'na vul., 3 # Naczv\'yazok HQ @ (30.1234, 50.5678)')
        child.expect('#')
        cbcl(child,'snmp-server contact Ivan Pylypenko +380501234567')
        child.expect('#')
        cbcl(child,'end')
        child.expect('#')
        cbcl(child,'exit')
        print ''
    except:
        print '\nException'
        child.interact()
    return None


