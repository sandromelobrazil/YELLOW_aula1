#!/usr/bin/python

import shodan
shodan_mykey= '7TeyFZ8oyLulHwYUOcSPzZ5w3cLYib61'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_host = shodan_api.host('3.220.87.155') 

print("COUNTRY")
print(shodan_host['country_name'])
print(shodan_host['country_code'])


print("TAG")
print(shodan_host['tags'])
for _tag in shodan_host['tags']:
    print(_tag)

'''
print("HOSTNAME")
print(shodan_host['hostname'])
for _host in shodan_host['hostname']:
    print(_host)
'''

print("HOSTNAMES")
print(shodan_host['hostnames'])
for _host in shodan_host['hostnames']:
    print(_host)


print("TAGS")
print(shodan_host['tags'])
print(shodan_host['org'])



print("PORTAS")
print(shodan_host['tags'])
#print(shodan_host['data'])

for _ports in shodan_host['data']:
    print("Portas", _ports['port'])


print("PORTAS | Protocolo ~ VERSAO")

for _ports in shodan_host['data']:
    print("Portas", _ports['port'],_ports['transport'], _ports['version'])


print("VULN")
print("DESCRICAO das VULNERABILIDADES")
for _vulns in shodan_host['vulns']:
    print("Vulnerabilities", _vulns)


'''
print("PORTAS | Protocolo | VERSAO | VULNERABILIDADES")

for _ports in shodan_host['data']:
    print("Portas", _ports['port'],_ports['transport'], _ports['version'])
    for _vulns in shodan_host['vulns']:
        print("Vulnerabilities", _vulns)
'''
'''
print("DESCRICAO das VULNERABILIDADES")
for info in shodan_host['data']['port']['vulns']:
    CVE = info.replace('!','')
    print("Vulnerabilidades:", info)
'''





'''

def shodan_portscan(shodan_host):
    for _ports in shodan_host['data']:
        _port_target = _ports['port']
        print("Portas identificadas:", _port_target)
        for info in shodan_host['hostname']:
            #print(info['data'])
            print(info)
        shodan_enumport = shodan_api.search('net:3.220.87.155  port:_porta_target')

        for info in shodan_enumport['matches']:
            print(info['data'])

shodan_portscan(shodan_host)

'''

