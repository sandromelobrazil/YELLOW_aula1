#!/usr/bin/python

import dns.zone
import dns.query
import dns.resolver
from datetime import datetime

myquery = dns.resolver.Resolver()

banner = '''
-------------------------- A V I S O  ----------------------------
|                                                                |
|   A tentativa de Transferencia de Zona em multiplos servidores |
|   pode pode ser uma tarefa demorada, sendo assim eh necessario |
|    paciencia... senao use o CTRL + C para cancelar!            |
|                                                                |
------------------------------------------------------------------
'''

print(banner)

def dns_getzone(_iptarget,_domain):
    try:
        zonetransfer = dns.zone.from_xfr(dns.query.xfr(_iptarget,_domain))
        #zonetransfer = dns.zone.from_xfr(dns.query.xfr(_iptarget,_domain, timeout=60.0))
    
        print("[*] - Tranferencia de Zona - Dominio:" + _domain + " \n")
        for _register in zonetransfer.nodes.keys():
            print(zonetransfer[_register].to_text(_register))

    except:
        print("[!] - FALHA - Tranferencia de Zona - Dominio:" + _domain + " \n")
        

def dns_checkipns(_nameserver,_domain):
    _nsip = myquery.query(_nameserver, 'A')

    for _ipdns in _nsip:
        print("[*] - DNS alvo:", _nameserver, "IP:", _ipdns)

        dns_getzone(str(_ipdns),_domain)


def dns_checkns(_domain):
    _answers = myquery.query(_domain, 'NS')
        
    for _ns in _answers:
        dns_checkipns(str(_ns),_domain)
                
time_start = datetime.now()
dns_checkns("megacorpone.com")

time_end = datetime.now()
time_attack = time_end - time_start
print("Tempo do Ataque:", time_attack)


