#!/usr/bin/python
import whois

target  = "google.com"
querywhois = whois.query(target)

print("Dominio: ", querywhois.name)

for _domain in querywhois.name_servers:
    print("Servidor de Nomes: " ,_domain)

print("Data de registro: ", querywhois.creation_date)
print("Data de Expiracao: ", querywhois.expiration_date)
print("Ultima Atualizacao: " , querywhois.last_updated)
print("Informacao de status: " , querywhois.status)
print("Registro Whois em: ", querywhois.registrar)
