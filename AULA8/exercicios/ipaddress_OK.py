#!/usr/bin/python
from threading import *
import ipaddress as ipaddress
from concurrent.futures import ThreadPoolExecutor

number_threads = 20


def testa_ip(_address):
    if '/' in _address:
        try:
            network_address = ipaddress.ip_network(_address)
        except:
            pass

    else:
        try:
            host_address = ipaddress.ip_address(_address)
        except:
            pass

def ler_ip(_wordlist):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break
            
            testa_ip(machine)

def run_threads(_wordlist):
    if number_threads >=2:
        with ThreadPoolExecutor(max_workers=number_threads) as criathreads:
            for _number  in range(1,number_threads):
                criathreads.submit(ler_ip, _wordlist=_wordlist)

    else:
        lista = Thread(target=ler_ip, args=(_wordlist,))
        lista.start()

run_threads('superlista.txt')


