#!/usr/bin/python

import nmap3
from datetime import datetime
from termcolor import colored

msg_ok1 = colored('[*]', 'green')
msg_ok2 = colored('[+]', 'cyan')
target = '11.11.11.171'

pynmap_Nmap = nmap3.Nmap()

def nmap_version():
    version_scan = pynmap_Nmap.nmap_version_detection(target)

    for _info in version_scan:
        print(msg_ok1,'- Porta:',_info['port'], '- Estado:', _info['state'],'- Flag:',_info['reason'],'- TTL:', _info['reason_ttl'])
    
        for chave,valor in _info['service'].items():
            if chave == 'method':
                pass
            elif chave == 'conf':
                pass
            else:
                print(msg_ok2, chave,':',valor)
    
        print()

nmap_start = datetime.now()
nmap_version()
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print(msg_ok1,'Tempo do Scan:', nmap_time)
