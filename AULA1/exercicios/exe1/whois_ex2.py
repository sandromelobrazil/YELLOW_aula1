#!/usr/bin/python

import whois

target = "google.com" 
querywhois = whois.query(target)

for _domain in querywhois.name_servers:
    print(_domain)


