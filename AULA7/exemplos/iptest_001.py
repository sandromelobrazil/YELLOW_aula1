#!/usr/bin/python

from threading import *
from datetime import datetime
import ipaddress

ipset = set()

def iptest(_iptarget):
    #global ipset
    try:
        ipaddress.ip_address(_iptarget)
        ipset.add(_iptarget)
        print( '[+] - IP alvo testado e armazenado', _iptarget)
    except:
        print('[-] - IP alvo descartado - formato errado', _iptarget)
    

def iplist(_iplist):
    with open(_iplist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break

            iptest(machine)
           

time_start = datetime.now()
iplist('ip_bugados')
time_end = datetime.now()
time_total = time_end - time_start
print(ipset)
print('[*] - Tempo total de execucao:', time_total)

#sort_ipset = sorted(ipset)
#for X in ipset:
#    print('======================> JA VALIDADO')
#    print(X)

