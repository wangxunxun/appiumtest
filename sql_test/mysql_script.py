#coding=utf-8
'''
Created on 2015年4月24日

@author: xun
'''
from sql_test import mysqlconnect
conn = mysqlconnect('69.164.202.55','test','test','test',3306).connect()
cur = conn.cursor()
print cur.execute('show tables')
result=cur.fetchall()
print result
cur.execute('select * from MESSAGE11')
result=cur.fetchall()
print result
print result[0][2]
i=90
while i<100:
    sql = 'insert into MESSAGE11 values(%d,%d,%d,%s,%s)'%(i,2322,2222,"34434343","454")
    cur.execute(sql)

    
    
    
    cur.execute('select * from MESSAGE11 where ID=%d' % i)
    i = i+1
    result=cur.fetchall()
    print result

cur.close()
conn.close()  