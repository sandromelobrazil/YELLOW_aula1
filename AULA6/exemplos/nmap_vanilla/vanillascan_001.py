#!/usr/bin/python

import nmap3
from datetime import datetime
from termcolor import colored

msg_ok1 = colored('[*]', 'green')
msg_ok2 = colored('==>[+]', 'cyan')
target = '11.11.11.171'

pynmap_scan = nmap3.NmapScanTechniques()
vanilla_scan = pynmap_scan.nmap_tcp_scan(target)


def nmap_vanillascan(_targetip):
    for _info in vanilla_scan[_targetip]:
        print(msg_ok1, _info['portid'], _info['protocol'], _info['state'],_info['reason'])

        for chave, valor in _info['service'].items():
            print(msg_ok2,chave, valor)
        print()


nmap_start = datetime.now()
nmap_vanillascan(target)
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print(msg_ok1,'Tempo do Scan:', nmap_time)
