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

def dns_aux(_word, _domain):
    dns_tipoa( _word + "." + _domain)


def dns_wordlist_ipv4(_wordlist):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break
            
            dns_aux(machine,domain)

def dns_portnum(numero):
    pass 

dns_wordlist_ipv4("word")
