#!/usr/bin/python

import pgdb

username = 'postgres'
pwd = 'postgres'
target = '11.11.11.171'
porttarget = 5432
dbtarget = 'postgres'

psqlconn = pgdb.Connection(user = username, password = pwd, host = target, port = porttarget, database = dbtarget)

print(psqlconn)

psqlconn.close()



