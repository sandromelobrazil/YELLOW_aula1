#!/usr/bin/python
import whois

target  = "google.com"
querywhois = whois.query(target)

print(querywhois.name)

for _domain in querywhois.name_servers:
    print(_domain)

print(querywhois.creation_date)
print(querywhois.expiration_date)
print(querywhois.last_updated)
print(querywhois.status)
print(querywhois.registrar)
