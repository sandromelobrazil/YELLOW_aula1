#!/usr/bin/python

import dns.zone
import dns.query
import dns.resolver

myquery = dns.resolver.Resolver()

def dns_getzone(_iptarget,_domain):
    print("Funcao dns_chekipns")
    zonetransfer = dns.zone.from_xfr(dns.query.xfr(_iptarget,_domain))

    for _register in zonetransfer.nodes.keys():
        print(zonetransfer[_register].to_text(_register))


def dns_checkipns(_nameserver,_domain):
    print("Funcao dns_chekipns")
    print(_nameserver)
    print(type(_nameserver))
    _nsip = myquery.query(_nameserver, 'A')

    for _ipdns in _nsip:
        print("IP do DNS", _ipdns)
        dns_getzone(str(_ipdns),_domain)


def dns_checkns(_domain):
    print("Funcao dns_chekns")
    _answers = myquery.query(_domain, 'NS')
        
    for _ns in _answers:
        print(_ns)
        print(type(_ns))
        _targetns = str(_ns)
        print(_targetns)
        print(type(_targetns))
        dns_checkipns(_targetns,_domain)
                

dns_checkns("yellow.dojo")

