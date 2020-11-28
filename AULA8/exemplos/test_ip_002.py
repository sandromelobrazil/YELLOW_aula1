#!/usr/bin/python
import ipaddress as ipaddress

listip = [ 'abs.1.2.', '1.1.1.1', '0.0.0.0', '255.255.255.255', '8.8.4.4', '192.168.0.255', '192.168.1.256', '300.1.1.1', 'a.b.c.d', '10.1.1.0/33', '1.1.1.1,32', '192.168.0.0/24', '172.16.0.0./16', '10.0.0.0/32' ]

for _iptarget in listip:
    if '/' in _iptarget:
        try:
            network_address = ipaddress.ip_network(_iptarget)
            print('[+] - Formato CDIR testado e validado para o endereco:', _iptarget)
        
        except:
            print('[!] - CDIR em formato invalido:', _iptarget)

    else:
        try:
            host_address = ipaddress.ip_address(_iptarget)
            print('[+] - Formato IP correto:', _iptarget)
        
        except:
            print('[-] - Formato IP INCORRETO:', _iptarget)

        
