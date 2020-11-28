#!/usr/bin/python
import ipaddress as ipaddress
from threading import *
from concurrent.futures import ThreadPoolExecutor


number_threads = 10


def testa_ip(_iptarget):
    if '/' in _iptarget:
        try:
            network_address = ipaddress.ip_network(_iptarget)
            print('[+] - Formato CDIR testado e validado para o endereco:', _iptarget)
        
        except:
            print('[!] - CDIR em formato invalido:', _iptarget)

    else:
        try:
            host_address = ipaddress.ip_address(_iptarget)
            print('[+] - Formato IP correto:', _iptarget)
        
        except:
            print('[-] - Formato IP INCORRETO:', _iptarget)


def run_scanlist(_wordlist):
    if number_threads >= 2:
        with ThreadPoolExecutor(max_workers=number_threads) as executor:
            for _number in range(1,number_threads):
                executor.submit(ler_ip, _wordlist=_wordlist)
                print('NOVA NOVA THREAD', _number)
    else:
        scanlist = Thread(target=testa_ip,args=(_iptarget,))
        scanlist.start()

def ler_ip(_wordlist):
    pass

    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break
            
            testa_ip(machine)
        

run_scanlist('superlista.txt')
