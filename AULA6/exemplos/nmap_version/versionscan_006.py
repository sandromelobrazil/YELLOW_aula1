#!/usr/bin/python

import nmap3

pynmap_version = nmap3.Nmap()
version_scan = pynmap_version.nmap_version_detection('11.11.11.171')

for _info in version_scan:
    print('[*] Porta:',_info['port'], '- Estado:', _info['state'],'- Flag:',_info['reason'],'- TTL:', _info['reason_ttl'])
    
    for chave,valor in _info['service'].items():
        print('-- [+]',chave,':',valor)
    
    print()

