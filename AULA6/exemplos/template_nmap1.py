#!/usr/bin/python

import nmap3
from datetime import datetime
from termcolor import colored

msg_ok1 = colored('[*]', 'green')
msg_ok2 = colored('[+]', 'cyan')
target = '11.11.11.171'

pynmap_Nmap = nmap3.Nmap()



nmap_start = datetime.now()
##
nmap_end = datetime.now()
nmap_time = nmap_end - nmap_start
print(msg_ok1,'Tempo do Scan:', nmap_time)
