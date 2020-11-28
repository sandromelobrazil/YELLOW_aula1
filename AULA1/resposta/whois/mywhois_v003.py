#!/usr/bin/python
### libraries
import whois

### skeletor libraries
import argparse
import sys
from pyfiglet import Figlet
from termcolor import colored

#### variaveis argpase
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


def func_whois(_domain):
    querywhois = whois.query(_domain)
    print(msg_ok,"Dominio: ", querywhois.name)

    for _domain in querywhois.name_servers:
        print(msg_ok, "Servidor de Nomes: " ,_domain)

    print(msg_ok,"Data de registro: ", querywhois.creation_date)
    print(msg_ok,"Data de Expiracao: ", querywhois.expiration_date)
    print(msg_ok,"Ultima Atualizacao: " , querywhois.last_updated)
    print(msg_ok,"Informacao de status: " , querywhois.status)
    print(msg_ok,"Registro Whois em: ", querywhois.registrar)
    

def func_main():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-d",'--domain', action="store", dest="domain",  help=msg_domain)
    option_args = option.parse_args()
    
    if option_args.domain == None:
        print(option.description)
        exit(0)

    domaintarget = option_args.domain
    func_whois(domaintarget)


if __name__ == '__main__':
    func_main()

