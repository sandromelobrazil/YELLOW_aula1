#!/usr/bin/python
import MySQLdb

target = '11.11.11.171'
user = 'root'
pwd = 'yodaninja'

myconn = MySQLdb.connect(host=target, user=user,password=pwd)

print(myconn)

myconn.close()



