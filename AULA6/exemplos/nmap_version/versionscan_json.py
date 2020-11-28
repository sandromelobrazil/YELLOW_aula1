#!/usr/bin/python

import nmap3
import json

pynmap_version = nmap3.Nmap()
version_scan = pynmap_version.nmap_version_detection('11.11.11.171')
type(version_scan)
version_json = json.dumps(version_scan, indent = 5)
print(version_json)

