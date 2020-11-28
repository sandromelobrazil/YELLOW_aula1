#!/usr/bin/python

import nmap3

pynmap_version = nmap3.Nmap()
version_scan = pynmap_version.nmap_version_detection('127.0.0.1')

print(type(version_scan)) # Retorna o tipo de objeto lista
print(version_scan) # Imprime a Lista
print(version_scan[0]) # Imprime o primeiro elemento da lista
print(type(version_scan[0])) # Imprime o tipo, neste caso o elemento é um dicionario

for _info in version_scan: #Percorre a lista
    print('Porta:',_info['port'], 'Estado:', _info['state'], _info['reason'], _info['reason_ttl'])

    for chave,valor in _info['service'].items():
        print('\t',chave,':',valor)
