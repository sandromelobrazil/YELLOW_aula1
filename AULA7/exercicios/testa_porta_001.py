#!/usr/bin/python
import argparse



msg_usage = 'vejas as opcoes abaixo:'

msg_manual = 'Informacoes de help com exemplos'  
msg_doc = '''  
==============================================================================================

Informe a porta, segue exemplo: \n
    --porta 22      ---> Para uma unica porta especifica.
    --porta 22-1000 ---> Para uma ranger de portas considerando a ordem da menor para maior

==============================================================================================
'''

msg_versao = "Versao Tabajara System 0.0001"

msg_porta = msg_usage





def  main_params():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-p","--porta" ,nargs= '+', dest="porta", help=msg_porta)
    option.add_argument("-m","--manual" , dest="manual", action='store_true', help=msg_manual)
    option.add_argument("-v","--versao" , dest="versao", action='store_true', help=msg_versao)
    
    option_args = option.parse_args()

    if option_args.porta == None:
        print(option.description)
       # exit(0)
    else:
        print('Portas')
        print(option_args.porta)
        print(type(option.description))

    if option_args.versao:
        print(msg_versao)

    if option_args.manual:
        print(msg_doc)


if __name__ == '__main__':
    main_params()
