#!/usr/bin/python

import dns.resolver

domain="uol.com.br"

dnsquery = dns.resolver.query(domain,"SOA")
for _domain in dnsquery:
    print("SOA - autoridade", _domain)

dnsquery = dns.resolver.query(domain,"NS")
for _domain in dnsquery:
    print("Servidor de Nomes", _domain)

dnsquery = dns.resolver.query(domain,"MX")
for _domain in dnsquery:
    print("Servidor Correio", _domain.exchange)

dnsquery = dns.resolver.query("games."+domain,"A")
for _domain in dnsquery:
    print("IP da maquina", _domain)

dnsquery = dns.resolver.query(domain,"TXT")
for _domain in dnsquery:
    print("Servidor Correio", _domain)


