#!/usr/bin/python

import json
import nmap3
from pygments import highlight, lexers, formatters

target = '11.11.11.171'
pynmap_scan = nmap3.NmapScanTechniques()
fin_scan = pynmap_scan.nmap_fin_scan(target)
finscan_json = json.dumps(fin_scan, indent = 5)
print(finscan_json)
