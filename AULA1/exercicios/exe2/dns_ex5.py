#!/usr/bin/python
import dns.resolver

domain="megacorpone.com" 
myquery = dns.resolver.Resolver()

def dns_tipoa(_host):
    try:
        _answers = myquery.query(_host, 'A')
    
        for _hostA in _answers:
            print("[+] Target:",_host, _hostA)
    
    except:
        pass

target = [ 'admin', 'www', 'www2', 'siem', 'vpn', 'zzz', 'intranet', ' extranet' ]

for _target in target:
    dns_tipoa( _target+".megacorpone.com")



