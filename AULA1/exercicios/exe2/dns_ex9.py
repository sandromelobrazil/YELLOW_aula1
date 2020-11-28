#!/usr/bin/python
import dns.resolver
from threading import *
from datetime import datetime

time_start = datetime.now()
domain="uol.com.br" 
myquery = dns.resolver.Resolver()


############### IPV4
def dns_tipoa_ipv4(_host):
    try:
        _answers = myquery.query(_host, 'A')
    
        for _hostA in _answers:
            print("[+] Target:",_host, _hostA)
    
    except:
        pass

def dns_aux_ipv4(_word, _domain):
    dns_tipoa_ipv4( _word + "." + _domain)


def dns_wordlist_ipv4(_wordlist):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break
            
            dns_aux_ipv4(machine,domain)

############### IPV6
def dns_tipoa_ipv6(_host):
    try:
        _answers = myquery.query(_host, 'AAAA')
    
        for _hostA in _answers:
            print("[+] Target:",_host, _hostA)
    
    except:
        pass

def dns_aux_ipv6(_word, _domain):
    dns_tipoa_ipv6( _word + "." + _domain)


def dns_wordlist_ipv6(_wordlist):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break
            
            dns_aux_ipv6(machine,domain)

fastdns_ipv4 = Thread(target=dns_wordlist_ipv4,args=("word1000",))
fastdns_ipv4.start()

fastdns_ipv6 = Thread(target=dns_wordlist_ipv6,args=("word1000",))
fastdns_ipv6.start()

#dns_wordlist_ipv4("word")
#dns_wordlist_ipv6("word")

time_end = datetime.now()
time_attack = time_end - time_start
print("Tempo do ataque:", time_attack)
