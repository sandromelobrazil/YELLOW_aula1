#!/usr/bin/python
import nmap3
import json

target = '11.11.11.171'
pynmap_scan = nmap3.NmapScanTechniques()
vanilla = pynmap_scan.nmap_tcp_scan(target)

vanilla_json = json.dumps(vanilla, indent = 5)
print(vanilla_json)

