#!/usr/bin/python
import nmap3
from datetime import datetime
from termcolor import colored

target = '11.11.11.171'
msg_ok1 = colored('[*]', 'green')
msg_ok2 = colored('==>[+]', 'cyan')

pynmap_banner = nmap3.Nmap()

def nmap_banner(_target):
    banner = pynmap_banner.nmap_version_detection(target)
    
    for _info in banner:
        print(msg_ok1,'Porta:',_info['port'])
        print(msg_ok2,'Protocolo:',_info['protocol'])
        print(msg_ok2,'Estado:', _info['state'])
        print(msg_ok2,'Razao',_info['reason'])
        print(msg_ok2,'TTL',_info['reason_ttl'])

        for chave, valor in _info['service'].items():
            if chave == 'method':
                pass
            elif chave == 'conf':
                pass
            else:
                print(msg_ok2, chave, valor)
        print()

nmap_start = datetime.now()
nmap_banner(target)
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print(msg_ok1,'Tempo do Scan:', nmap_time)

