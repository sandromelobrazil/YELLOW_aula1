#!/usr/bin/python
import nmap3
from datetime import datetime
from termcolor import colored

msg_ok1 = colored('[*]', 'green')
msg_ok2 = colored('==>[+]', 'cyan')
target = '11.11.11.171'

pynmap_scan = nmap3.NmapScanTechniques() 
fin_scan = pynmap_scan.nmap_fin_scan(target)

def nmap_finscan(_targetip):
    _porta = fin_scan['ports']['portid']
    _name = fin_scan['ports']['service']['name']
    _state = fin_scan['ports']['state']['state']
    _reason = fin_scan['ports']['state']['reason']
    _reason_ttl = fin_scan['ports']['state']['reason_ttl']
    
    print(msg_ok1, 'Porta:', _porta)
    print(msg_ok2, 'Servico:', _name)
    print(msg_ok2, 'Estado', _state)
    print(msg_ok2, 'Razao:', _reason)
    print(msg_ok2, 'TTL:', _reason_ttl)
    print()



nmap_start = datetime.now()
nmap_finscan(target)
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print(msg_ok1,'Tempo do Scan:', nmap_time)
