#!/usr/bin/python3.6
import pythonwhois  

pywhois = pythonwhois

domains = ['google.com', 'stackoverflow.com']
for dom in domains:
    details = pywhois.get_whois(dom)
    print(details['contacts']['registrant'])
