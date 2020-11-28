#!/usr/bin/python
import ipaddress as ipaddress


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

        

def ler_ip(_wordlist):
    pass

    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break
            
            testa_ip(machine)

ler_ip('superlista.txt')
