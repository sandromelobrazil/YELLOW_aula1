#!/usr/bin/python

import nmap3
target = '11.11.11.171'

pynmap_scan = nmap3.NmapScanTechniques()
fin_scan = pynmap_scan.nmap_fin_scan(target)


print("Porta:", fin_scan['ports']['portid'])
print("Protocolo:", fin_scan['ports']['protocol'])
print("Estado:", fin_scan['ports']['state']['state'])
print("Razao:", fin_scan['ports']['state']['reason'])
print("TTL:", fin_scan['ports']['state']['reason_ttl'])
print("Servicos:", fin_scan['ports']['service']['name'])




