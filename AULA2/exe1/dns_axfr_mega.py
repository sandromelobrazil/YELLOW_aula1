#!/usr/bin/python

import dns.zone
import dns.query

target = "3.211.51.86"
domain = "megacorpone.com" 

zonetransfer = dns.zone.from_xfr(dns.query.xfr(target,domain))

for _register in zonetransfer.nodes.keys():
    print(zonetransfer[_register].to_text(_register))

