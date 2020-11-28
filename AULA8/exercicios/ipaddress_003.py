#!/usr/bin/python

import ipaddress as ipaddress

def testa_ip(_address):
    if '/' in _address:
        try:
            network_address = ipaddress.ip_network(_address)
            print('[+] - Formato de endereco de rede correto (CDIR APROVADO)', _address)

        except:
            print('[!] - Formato de endereco de rede INCORRETO (CDIR REPROVADO)', _address)

    else:
        try:
            host_address = ipaddress.ip_address(_address)
            print('[+] - Formato de endereco IP CORRETO:', _address)

        except:
            print('[-] - Formato de endereco IP INCORRETO:', _address)


def ler_ip(_wordlist):
    with open(_wordlist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break
            
            testa_ip(machine)

ler_ip('superlista.txt')


