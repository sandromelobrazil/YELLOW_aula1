#!/usr/bin/python
import nmap3
import json

target = '11.11.11.171'

pynmap_banner = nmap3.Nmap()
nmap_banners = pynmap_banner.nmap_version_detection(target)

nmapbanners_json = json.dumps(nmap_banners, indent = 5)
print(nmapbanners_json)

