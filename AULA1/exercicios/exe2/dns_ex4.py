#!/usr/bin/python
import dns.resolver

domain="megacorpone.com" 
myquery = dns.resolver.Resolver()

def dns_tipoa(_host):
    _answers = myquery.query(_host, 'A')
    
    for _hostA in _answers:
        print("[+] Target:", _hostA)
        

dns_tipoa("admin.megacorpone.com")



