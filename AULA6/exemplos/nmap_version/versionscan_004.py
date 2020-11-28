#!/usr/bin/python

import nmap3

pynmap_version = nmap3.Nmap()
version_scan = pynmap_version.nmap_version_detection('11.11.11.171')

for _info in version_scan: #Percorre a lista
    for chave,valor in _info['service'].items():
        if chave == 'extrainfo':
            print(chave, valor)

