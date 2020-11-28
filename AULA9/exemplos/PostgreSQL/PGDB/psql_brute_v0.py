#!/usr/bin/python3.7
import pgdb

psqlconn = pgdb.Connection(user = "postgres", password = "postgres", host = "10.171.1.129", port = "5432", database = "postgres")

print(psqlconn)

psqlconn.close()



