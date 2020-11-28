#!/usr/bin/python
import nmap3
import json

target = '11.11.11.171'
pynmap_scan = nmap3.NmapScanTechniques()
udpscan = pynmap_scan.nmap_udp_scan(target)

udpscan_json = json.dumps(udpscan, indent = 5)
print(udpscan_json)

