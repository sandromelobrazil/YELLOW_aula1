#!/usr/bin/python3.7
import psycopg2
#from psycopg2 import connect 

#postgreconn = connect(user = "postgres", password = "postgres", host = "127.0.0.1", port = "5432", database = "postgres_db")
postgreconn = psycopg2.connect(user = "postgres", password = "postgres", host = "10.171.1.129", port = "5432", database = "postgres")

prompt = postgreconn.cursor()
print(prompt)

prompt.execute("Select version();")
version = prompt.fetchone()
print("PostgreSQL version enumeration: \n" + str(version) + "\n")

propriety = postgreconn.get_dsn_parameters()
print("Generic information about the PostgreSQL connection: ")
print(propriety)

postgreconn.close()



