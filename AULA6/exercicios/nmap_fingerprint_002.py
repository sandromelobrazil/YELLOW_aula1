#!/usr/bin/python
import nmap3 
from datetime import datetime
from termcolor import colored

msg_ok1 = colored('[*]', 'green')
msg_ok2 = colored('->[+]', 'cyan')

pynmap_os = nmap3.Nmap()
target = '11.11.11.171'

def nmap_fingerprint(_target):
    fingerprint = pynmap_os.nmap_os_detection(_target)

    for _os in fingerprint:
        print(msg_ok1,'Sistema Operaciona',_os['name'])
        print(msg_ok2,'Possibilidade:',_os['accuracy'],'%')
        print(msg_ok2,'Tipo:',_os['osclass']['type'])
        print(msg_ok2,'Vendor:',_os['osclass']['vendor'])
        print(msg_ok2, 'Familia:',_os['osclass']['osfamily'])
        print(msg_ok2,'Geracao:',_os['osclass']['osgen'])
        print(msg_ok1,'Common Platform Enumeration:',_os['cpe'])


nmap_start = datetime.now()
##
nmap_fingerprint(target)
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print(msg_ok1,'Tempo do Scan:', nmap_time)
