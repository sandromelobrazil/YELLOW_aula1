#!/usr/bin/python
import nmap3
from datetime import datetime
from termcolor import colored

target = '11.11.11.171'
msg_ok1 = colored('[*]', 'green')
msg_ok2 = colored('==>[+]', 'cyan')

pynmap_scan = nmap3.NmapScanTechniques()
tcpsyn = pynmap_scan.nmap_syn_scan(target)

def nmap_tcpsyn(_target):
    for _info in tcpsyn[_target]:
        print(msg_ok1,'Porta:',_info['portid'])
        print(msg_ok2,'Protocolo:',_info['protocol'])
        print(msg_ok2,'Estado:', _info['state'])
        print(msg_ok2,'Razao',_info['reason'])
        print(msg_ok2,'TTL',_info['reason_ttl'])

        for chave, valor in _info['service'].items():
            if chave == 'name':
                print(msg_ok2, chave, valor)
        print()

nmap_start = datetime.now()
nmap_tcpsyn(target)
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print(msg_ok1,'Tempo do Scan:', nmap_time)

