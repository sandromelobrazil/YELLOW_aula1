#!/usr/bin/python
import nmap3
import json
from datetime import datetime
from termcolor import colored

target = '11.11.11.171'
pynmap_scan = nmap3.NmapScanTechniques() 
vanilla_scan = pynmap_scan.nmap_tcp_scan(target)
vanilla_json = json.dumps(vanilla_scan, indent = 5)
print(vanilla_json)

