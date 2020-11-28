#!/usr/bin/python

import nmap3

target = '11.11.11.171'


##############################################################################################################
#### PING SCAN
pynmap_scan = nmap3.NmapScanTechniques()

def linha(_number):
    print('=' * _number)

linha(40)
linha(40)

linha(40)
linha(40)

#### Tecnicas de varreduras

pynmap_scan = nmap3.NmapScanTechniques() 
pingscan = pynmap_scan.nmap_ping_scan(target)

for _ping in pingscan:
    print(_ping['state'])
    print(_ping['reason'])

for _ping in pingscan:
    for _addr in _ping['addresses']:
        print(_addr)
 
for _ping in pingscan:
    for _addr in _ping['addresses']:
        print(_addr['addr'])
        print(_addr['addrtype'])



##############################################################################################################
linha(40)
linha(40)




##### TCP Connect Scan - Vanila Scan
print ('TCP CONNECT - VANILLA SCAN')

vanilla_scan = pynmap_scan.nmap_tcp_scan(target)

for _info in vanilla_scan['11.11.11.171']:
    print(_info['portid'])
    print(_info['protocol'])
    print(_info['state'])
    print(_info['reason'])


linha(40)

for _info in vanilla_scan['11.11.11.171']:
    print(_info['portid'], _info['protocol'], _info['state'],_info['reason'])


##############################################################################################################
linha(40)
print ('TCP SYN  - STHEALTH  SCAN')

syn_scan = pynmap_scan.nmap_syn_scan(target)
for _info in syn_scan:
    print(_info)


for _info in syn_scan['11.11.11.171']:
    print(_info['portid'], _info['protocol'], _info['state'],_info['reason'])


linha(40)
print ('STHEALTH  SCAN')

stealth_scan = pynmap_scan.nmap_stealth_scan(target)
for _info in stealth_scan:
    print(_info)


for _info in stealth_scan['11.11.11.171']:
    print(_info['portid'], _info['protocol'], _info['state'],_info['reason'])

##############################################################################################################
linha(40)
print ('TCP FIN')

fin_scan = pynmap_scan.nmap_fin_scan(target)

for _info in fin_scan:
...     print(_info)


<linha(40)
##### FIN SCAN

print ('TCP FIN')

fin_scan = pynmap_scan.nmap_fin_scan(target)

for _info in fin_scan:
    print(_info)
####################

print(fin_scan['ports']['protocol'])
print(fin_scan['ports']['portid'])
print(fin_scan['ports']['state'])
print(fin_scan['ports']['service'])


####################
print(fin_scan['ports']['state']['state'])
print(fin_scan['ports']['state']['reason'])
print(fin_scan['ports']['state']['reason_ttl'])


####################

_porta = fin_scan['ports']['portid'])
_name = fin_scan['ports']['service']['name']
_state = fin_scan['ports']['state']['state']
_reason = fin_scan['ports']['state']['reason']
_reason_ttl = fin_scan['ports']['state']['reason_ttl']



<linha(40)
##### UDP SCAN

#>>> import nmap3
#>>> pynmap_scan = nmap3.NmapScanTechniques()
#>>> 
#>>> udp_scan = pynmap_scan.nmap_udp_scan('11.11.11.171')
#>>> 
#>>> type(udp_scan)
#<class 'dict'>
#>>> 
#>>> import json
#>>> udp_json = json.dumps(udp_scan, indent = 5)
#>>> print(udp_json)

for _info in udp_scan['11.11.11.171']:
    print(_info['portid'], _info['state'], _info['reason'], _info['reason_ttl'])







linha(40)
linha(40)
######## OS Enumeration

#### IDE
import nmap3
pynmap_version = nmap3.Nmap()
target = '11.11.11.171'
version_scan = pynmap_version.nmap_version_detection(target)
type(version_scan)
import json
version_json = json.dumps(version_scan, indent = 5)
print(version_json


Porta: 22 Estado: open Flag syn-ack TTL: 0
         name : ssh
         product : OpenSSH
         version : 8.3p1 Debian 1
         extrainfo : protocol 2.0
         ostype : Linux





pynmap_version = nmap3.Nmap()
version_scan = pynmap_version.nmap_version_detection('11.11.11.171')


for _info in version_scan:
    print(_info['port'], _info['state'], _info['reason'], _info['reason_ttl'])
######

for _info in version_scan:
    print(_info['port'], _info['state'], _info['reason'], _info['reason_ttl'])
    for item in _info['service']:


for _info in version_scan:
    print(_info['service'])


linha(40)
linha(40)
######## OS Fingerprint
pynmap_os = nmap3.Nmap()
os_fingerprint = pynmap_os.nmap_os_detection('11.11.11.171')

for os in os_fingerprint:
    print(os['name'])
    print(os['accuracy'])
    print(os['osclass']['type'])
    print(os['osclass']['vendor'])
    print(os['osclass']['osfamily'])
    print(os['osclass']['osgen'])
    print(os['cpe'])


linha(40)
linha(40)

linha(40)
##### Metodo nmap_dns_brute_script
pynmap = nmap3.Nmap()
results = pynmap.nmap_dns_brute_script('uol.com.br')
'''



linha(40)
##### Metodo nmap_args
#i>>> import json
#>>> import nmap3
#>>> pynmap = nmap3.Nmap()
#>>> target = '11.11.11.171'
#>>> 
#>>> nmap_args = pynmap.scan_top_ports(target,args='-sC')
#>>> nmap_arsjson = json.dumps(nmap_args, indent = 5)
#>>> print(nmap_arsjson)



for _info in nmap_args:
    print(_info['port'], _info['state'], _info['reason'], _info['reason_ttl'])
    for item in _info['service']:


