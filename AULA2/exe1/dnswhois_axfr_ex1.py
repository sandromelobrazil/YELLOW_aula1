#!/usr/bin/python

import dns.zone
import dns.query
import dns.resolver
import whois

myquery = dns.resolver.Resolver()

def dns_getzone(_iptarget,_domain):
    try:
        zonetransfer = dns.zone.from_xfr(dns.query.xfr(_iptarget,_domain))
    
        print("\n [*] - Tranferencia de Zona - Dominio:" + _domain + " \n")
        for _register in zonetransfer.nodes.keys():
            print(zonetransfer[_register].to_text(_register))

    except:
        print("\n [!] - FALHA - Tranferencia de Zona - Dominio:" + _domain + " \n")
        pass 

    return

def dns_checkipns(_nameserver,_domain):
    _nsip = myquery.query(_nameserver, 'A')

    for _ipdns in _nsip:
        print("IP do DNS", _ipdns)
        dns_getzone(str(_ipdns),_domain)


def whois_ns(_domain):
    try:
        querywhois = whois.query(_domain)

        for _whois_ns in querywhois.name_servers:
            print(_whois_ns)
            print(type(_whois_ns))
            dns_checkipns(_whois_ns,_domain)
    
    except:
        print("Dominio foi digitado errado ou nao exite")
        pass

whois_ns("globo.com")
