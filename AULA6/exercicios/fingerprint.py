#!/usr/bin/python
import nmap3
import json

target = '11.11.11.171'
pynmap_scan = nmap3.Nmap()

fingerprint = pynmap_scan.nmap_os_detection(target)

fingerprint_json = json.dumps(fingerprint, indent = 5)
print(fingerprint_json)

