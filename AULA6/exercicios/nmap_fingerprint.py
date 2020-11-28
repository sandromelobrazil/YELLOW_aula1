#!/usr/bin/python
import nmap3 

pynmap_os = nmap3.Nmap()
target = '11.11.11.171'
fingerprint = pynmap_os.nmap_os_detection(target)

for _os in fingerprint:
    print('Sistema Operaciona',_os['name'])
    print('Possibilidade:',_os['accuracy'],'%')
    print('Tipo:',_os['osclass']['type'])
    print('Vendor:',_os['osclass']['vendor'])
    print('Familia:',_os['osclass']['osfamily'])
    print('Geracao:',_os['osclass']['osgen'])
    print('Common Platform Enumeration:',_os['cpe'])
