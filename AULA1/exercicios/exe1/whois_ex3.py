#!/usr/bin/python

import whois

def func_whois(_domain):
    querywhois = whois.query(_domain)
    for _domain in querywhois.name_servers:
        print("Servidor NDS:",_domain)

    print("Data de registro:", querywhois.creation_date)
    print("Data de Expiracao:", querywhois.expiration_date)
    print("Ultima atualizacao:", querywhois.last_updated)
    print("Registro Whois em:", querywhois.registrar)

func_whois("google.com")


