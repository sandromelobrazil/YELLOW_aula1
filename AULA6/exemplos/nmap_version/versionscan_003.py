#!/usr/bin/python

import nmap3

pynmap_version = nmap3.Nmap()
version_scan = pynmap_version.nmap_version_detection('127.0.0.1')

for _info in version_scan: #Percorre a lista
    print('Porta:',_info['port'], 'Estado:', _info['state'], 'Flag',_info['reason'],'TTL:', _info['reason_ttl'])

    for chave,valor in _info['service'].items():
        print('\t',chave,':',valor)
