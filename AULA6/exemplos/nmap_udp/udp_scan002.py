#!/usr/bin/python
import nmap3
from datetime import datetime
from termcolor import colored

msg_ok1 = colored('[*]', 'green')
msg_ok2 = colored('==>[+]', 'cyan')
target = '11.11.11.171'

pynmap_scan = nmap3.NmapScanTechniques() 
udp_scan = pynmap_scan.nmap_udp_scan(target)

def nmap_udpscan(_targetip):
    
    for _info in udp_scan[_targetip]:
        print(msg_ok1,_info['portid'], _info['state'], _info['reason'], _info['reason_ttl'])

        for chave, valor in _info['service'].items():
            if chave == 'method' or chave == 'conf':
                pass
            else:
                print(msg_ok2,chave,':',valor)
    
        print()

    for chave, valor in udp_scan['runtime'].items():
        if chave == 'summary':
            _sum = valor
            print(_sum)

nmap_start = datetime.now()
nmap_udpscan(target)
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print(msg_ok1,'Tempo do Scan:', nmap_time)
