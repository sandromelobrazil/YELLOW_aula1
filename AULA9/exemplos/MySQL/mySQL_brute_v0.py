#!/usr/bin/python3.7
import MySQLdb
mysqlconn = MySQLdb.connect(host='10.171.1.129',user='root',password='yodaninja')
print(mysqlconn)
mysqlconn.close()

