#!/usr/bin/python

import dns.zone
import dns.query

target = "11.11.11.171"
domain = "yellow.dojo" 

zonetransfer = dns.zone.from_xfr(dns.query.xfr(target,domain))

for _register in zonetransfer.nodes.keys():
    print(zonetransfer[_register].to_text(_register))

