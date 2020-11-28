#!/usr/bin/python

import nmap3

pynmap_version = nmap3.Nmap()
version_scan = pynmap_version.nmap_version_detection('11.11.11.171')

for _info in version_scan: #Percorre a lista
    for chave,valor in _info['service'].items():
        if chave == 'name':
            _name = valor

        if chave == 'product':
            _product = valor

        if chave == 'version':
            _version = valor
        #if chave == 'extrainfo':
         #   _extrainfo = valor

        if chave == 'ostype':
            _ostype = valor 

    print('Porta:',_info['port'], '- Estado:', _info['state'],'- Servico:',_name,'- Product:', _product, '- Version:',_version, '- Fingerprint:', _ostype,'- Flag:',_info['reason'],'- TTL:', _info['reason_ttl'])
