#!/usr/bin/python

import whois
### skeletor libraries
import argparse
import sys
from pyfiglet import Figlet
from termcolor import colored

#### variaveis argpase - skeletor
nome_app = str(sys.argv[0])
msg_usage = "\n Usage: python3 " + nome_app + " -d <dominio alvo> \n" 
msg_domain = "Informe o dominio alvo" 
### variaveis do banner
msg_font=('puffy')
msg_banner="myWHOIS" 
msg_banner_custom = Figlet(font=msg_font)
msg_banner_color=colored(msg_banner_custom.renderText(msg_banner), 'white')
msg_ok=colored('[+] - ','green') 

print(msg_banner_color)
print(" -------------------------------------------------------------------> v.01")
print()
### skeletor

################ Inicio do seu codigo

def func_whois(_domain):
    querywhois = whois.query(_domain)
    for _domain in querywhois.name_servers:
        print("Servidor NDS:",_domain)

    print("Data de registro:", querywhois.creation_date)
    print("Data de Expiracao:", querywhois.expiration_date)
    print("Ultima atualizacao:", querywhois.last_updated)
    print("Registro Whois em:", querywhois.registrar)

################ Fim do seu codigo
    

def func_main():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-d",'--domain', action="store", dest="domain",  help=msg_domain)
    option.add_argument("-v",'--version', action="store", dest="version",  help='Version 0.1')
    option_args = option.parse_args()
    
    if option_args.domain == None:
        print(option.description)
        exit(0)
    
'''
    if option_args.version != None:
        print("Version 0.1")
        exit(0)
'''
    domaintarget = option_args.domain
    func_whois(domaintarget)


if __name__ == '__main__':
    func_main()

