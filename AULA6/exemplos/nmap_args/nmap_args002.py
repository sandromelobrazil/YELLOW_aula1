#!/usr/bin/python

import nmap3
from termcolor import colored

msg_ok1 = colored('[*]', 'green')
msg_ok2 = colored('--> [+]', 'cyan')
target = '11.11.11.171'

pynmap = nmap3.Nmap()
nmap_args = pynmap.scan_top_ports(target,args='-sC -n -T5')

def nmap_argstop(_targetip):
    for _info in nmap_args[_targetip]:
        print(msg_ok1,_info['portid'], _info['state'], _info['reason'], _info['reason_ttl'])
        
        for chave, valor in _info['service'].items():
            if chave == 'method' or chave == 'conf':
                pass
            else:
                print(msg_ok2,chave,':',valor)
    
        print()

    for chave, valor in nmap_args['runtime'].items():
        if chave == 'summary':
            _sum = valor
            print(_sum)



nmap_argstop(target)
