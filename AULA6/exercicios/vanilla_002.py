#!/usr/bin/python
import nmap3

target = '11.11.11.171'
pynmap_scan = nmap3.NmapScanTechniques()
vanilla = pynmap_scan.nmap_tcp_scan(target)

for _info in vanilla[target]:
    print(_info['portid'])
    print(_info['protocol'])
    print(_info['state'])
    print(_info['reason'])

    for chave, valor in _info['service'].items():
        print(chave, valor)

    print()


