#!/usr/bin/python

### skeletor libraries
import argparse
import sys
import time
import nmap3
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime 

#### variaveis argpase - skeletor
nome_app = str(sys.argv[0])
msg_usage = "\n Usage: python3 " + nome_app + " -p  <ip alvo> \n" 
msg_domain = "Informe o dominio alvo" 
### variaveis do banner
msg_font=('puffy')
msg_banner="pyNMAP Ninja plu plus turbo" 
msg_banner_custom = Figlet(font=msg_font)
msg_banner_color=colored(msg_banner_custom.renderText(msg_banner), 'green')

#### Outras variave
msg_ast=colored('[*]', 'yellow')
msg_int=colored('[!]', 'blue')
msg_ok=colored('[+]', 'green')
msg_ok1=colored('[+]', 'green')
msg_ok2=colored('[+] ==>', 'cyan')
msg_fail=colored('[-]', 'red')

option_msg = ' ==================> AINDA NAO IMPLEMENTADO' 
msg_target = 'Define o IP alvo'
msg_file = 'Informe o arquivo com a lista de IP'
msg_version = 'Inform a versao do Script'
msg_port = 'Informe a porta/s alvo -p 22 ou uma range -p 22-100'
msg_banner = 'Possibilita a leitura de Banners'
msg_vanilla = 'Varredura Vanilla Scan'
msg_tcpsyn = 'Varredura TCP Steulth' 
msg_fingerprint = 'Fingerprint - Detecao do SO' 
msg_udp = 'Varredura UDP'


#### METODOS - CLASSES
pynmap_scan = nmap3.NmapScanTechniques()
pynmap_nmap3 = nmap3.Nmap()

### skeletor

################ Inicio do seu codigo
###==> Auxiliares
### ===> Versao 
def versao():
    print(msg_banner_color)
    print(" -------------------------------------------------------------------> v.01")
    print()

### ===> Funcao checkip
### ===> Funcao ler arquivo
### ===> Funcao execucao com 1 thread
### ===> Funcao execucao com multipl<as thread

### ===> Funcao implementacao
def  linha(_cara, _number):
    print(_cara * _number)

def  naopronta():
    linha('=', 30)
    print()
    print(' AINDA EM DESENVOLVIMENTO ')
    print()
    linha('=', 30)

###==> Auxiliares

##### Funcao Vanilla SCAN -sT
def nmap_vanilla(_target,_options):
    vanilla = pynmap_scan.nmap_tcp_scan(_target,args=_options)

    for _info in vanilla[_target]:
        print(msg_ok1,'Porta:',_info['portid'])
        print(msg_ok2,'Protocolo:',_info['protocol'])
        print(msg_ok2,'Estado:', _info['state'])
        print(msg_ok2,'Razao',_info['reason'])

        for chave, valor in _info['service'].items():
            if chave == 'name':
                print(msg_ok2, chave, valor)
        print()
##### Funcao Vanilla SCAN

##### Funcao TCP SYN -sS

def nmap_tcpsyn(_target, _options):
    tcpsyn = pynmap_scan.nmap_syn_scan(_target,args=_options)

    for _info in tcpsyn[_target]:
        print(msg_ok1,'Porta:',_info['portid'])
        print(msg_ok2,'Protocolo:',_info['protocol'])
        print(msg_ok2,'Estado:', _info['state'])
        print(msg_ok2,'Razao',_info['reason'])
        print(msg_ok2,'TTL',_info['reason_ttl'])

        for chave, valor in _info['service'].items():
            if chave == 'name':
                print(msg_ok2, chave, valor)
        print()
##### Funcao TCP SYN

##### Funcao Banner Version -sV
def nmap_banner(_target, _options):
    banner = pynmap_nmap3.nmap_version_detection(_target, _options)
    
    for _info in banner:
        print(msg_ok1,'Porta:',_info['port'])
        print(msg_ok2,'Protocolo:',_info['protocol'])
        print(msg_ok2,'Estado:', _info['state'])
        print(msg_ok2,'Razao',_info['reason'])
        print(msg_ok2,'TTL',_info['reason_ttl'])

        for chave, valor in _info['service'].items():
            if chave == 'method':
                pass
            elif chave == 'conf':
                pass
            else:
                print(msg_ok2, chave, valor)
        print()
##### Funcao Banner Version


##### Funcao Fingerprint -O
def nmap_fingerprint(_target):
    fingerprint = pynmap_nmap3.nmap_os_detection(_target)

    for _os in fingerprint:
        print(msg_ok1,'Sistema Operaciona',_os['name'])
        print(msg_ok2,'Possibilidade:',_os['accuracy'],'%')
        print(msg_ok2,'Tipo:',_os['osclass']['type'])
        print(msg_ok2,'Vendor:',_os['osclass']['vendor'])
        print(msg_ok2, 'Familia:',_os['osclass']['osfamily'])
        print(msg_ok2,'Geracao:',_os['osclass']['osgen'])
        print(msg_ok1,'Common Platform Enumeration:',_os['cpe'])

##### Funcao Fingreprint


##### Funcao UDP SCAN -sU
def nmap_udp(_target, _porta):
    udpscan = pynmap_scan.nmap_udp_scan(_target,args='-p'+str(_porta))

    for _info in udpscan[_target]:
        print(msg_ok1,_info['portid'])
        print(msg_ok2,_info['protocol'])
        print(msg_ok2,_info['state'])
        print(msg_ok2,_info['reason'])
        print(msg_ok2,_info['reason_ttl'])
    
        for chave, valor in _info['service'].items():
            if chave == 'method':
                pass
            
            elif chave == 'conf':
                pass

            else:
                print(msg_ok2, chave, valor)

        print()


##### Funcao UDP SCAN



################ Fim do seu codigo
    

def func_main():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-t",'--target', dest="target",  help=msg_target)
    option.add_argument("-f",'--file', dest="file",  help=msg_file)
    option.add_argument("-p",'--port',  dest="ports",  help=msg_port)
    option.add_argument("-sT",'--vanilla',  dest="vanilla",  help=msg_vanilla, action='store_true')
    option.add_argument("-sS",'--tcpsyn',  dest="tcpsyn",  help=msg_tcpsyn, action='store_true')
    option.add_argument("-sV",'--banner',  dest="banner",  help=msg_banner, action='store_true')
    option.add_argument("-O",'--fingerprint',  dest="fingerprint",  help=msg_fingerprint, action='store_true')
    option.add_argument("-sU",'--udp',  dest="udp",  help=msg_udp, action='store_true')
    option.add_argument("-v",'--version',  dest="version",  help=msg_version, action='store_true')
    option_args = option.parse_args()

    versao()
    
    if option_args.version:
        versao()

    if option_args.target == None:
        print(option.description)
        exit(0)
        
    targetip = option_args.target
    fileip = option_args.file
    
    if option_args.vanilla:
        nmap_vanilla(targetip,'-F')

    if option_args.tcpsyn:
        nmap_tcpsyn(targetip,'-F')

    if option_args.banner:
        nmap_banner(targetip,'-sV -F')

    if option_args.fingerprint:
        nmap_fingerprint(targetip)

    if option_args.udp:
        nmap_udp(targetip,'53,111,137,138')

if __name__ == '__main__':
    func_main()

