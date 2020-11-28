#!/usr/bin/python

import ipaddress as ipaddress

listip = [ '1.1.11.1', 'a.b.c.d', '0.0.0.0', '255.255.255.255', '1.0.0.257', '192.168.0.0/24', '10.0.0.1/32', '11.11.1.1/33', '176.16.0,5', '1.3.1.', '19.19.1.1..', '19.1.1.0/35', '3.333.33.3/45' ]

for _address in listip:
    if '/' in _address:
        try:
            network_address = ipaddress.ip_network(_address)
            print('[+] - Formato de endereco de rede correto (CDIR APROVADO)', _address)

        except:
            print('[!] - Formato de endereco de rede INCORRETO (CDIR REPROVADO)', _address)
