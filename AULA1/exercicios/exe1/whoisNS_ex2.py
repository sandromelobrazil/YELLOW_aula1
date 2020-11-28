#!/usr/bin/python

import whois

target = "google.com" 
querywhois = whois.query(target)

def whois_ns(_domain):
    for _whois_ns in querywhois.name_servers:
        print(_whois_ns)

whois_ns(target)
