#!/usr/bin/python
import nmap3
import json

target = '11.11.11.171'
pynmap_scan = nmap3.NmapScanTechniques()
tcpsyn = pynmap_scan.nmap_syn_scan(target)

tcpsyn_json = json.dumps(tcpsyn, indent = 5)
print(tcpsyn_json)

