import argparse
msg_arg='DNS Python - Register Enumeration'

def func_main():
    parser = argparse.ArgumentParser(description=msg_arg)
    parser.add_argument('--domain', action="store", dest="domain",  default=domain)
    option = parser.parse_args() 
    domaintarget = option.domain
    func_dnsfoot(domaintarget)


if __name__ == '__main__':
    func_main()


