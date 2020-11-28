#!/usr/bin/python
import nmap3
import json
from datetime import datetime
from termcolor import colored

target = '11.11.11.171'
pynmap_scan = nmap3.NmapScanTechniques() 
udp_scan = pynmap_scan.nmap_udp_scan(target)
version_json = json.dumps(udp_scan, indent = 5)
print(version_json)

