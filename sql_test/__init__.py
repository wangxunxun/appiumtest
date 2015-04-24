#coding=utf-8
'''
Created on 2015年4月24日

@author: xun
'''
import MySQLdb


class mysqlconnect:
    def __init__(self,host,user,passwd,db,port):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        
    def connect(self):
        conn=MySQLdb.connect(self.host,self.user,self.passwd,self.db,self.port)
        
        return conn
    
    
if __name__ == "__main__":  
    conn = mysqlconnect('69.164.202.55','test','test','test',3306).connect()
    cur = conn.cursor()
    print cur.execute('show tables like "MESSAGE1"')