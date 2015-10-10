#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'DanielSong'

import mysql.connector
import generate200Keys 

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'codingtest',
  'raise_on_warnings': True,
}

class save_keys_to_mysql:
	def __init__(self,path):
		self.path=path
		print(self.path)
	def __conn(self,**conf):
		try:
			conn=mysql.connector.connect(**conf)
			print(conn)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("database does not exists")
			else:
				print("we met error\r\n")
				print(err)
		return conn
		#print(self.conn)

	def save_to_mysql(self,key_array,**conf):
		conn=self.__conn(**conf)
		path=self.path
		cursor=conn.cursor()
		cursor.execute('drop table if exists act_keys')
		cursor.execute('create table act_keys (id int(8) primary key, act_keys varchar(50))')
		row=0
		#with open('keys_text.txt','r') as f:
		#	for line in f.readlines():
		for onekey in key_array:
				#row_no='0000'+str(row)
				#act_keys=line.rstrip()
				cursor.execute('insert into act_keys (id, act_keys) values (%s, %s)',[row,onekey])
				row+=1
		conn.commit()
		cursor.close()
		conn.close()


	def see_all(self,**conf):
		conn=self.__conn(**conf)
		cursor=conn.cursor()
		cursor.execute('select * from act_keys')
		values=cursor.fetchall()
		print(values)
		cursor.close()
		conn.close()


if __name__ == '__main__':
    #    print("a")
    codeStr = []
    for i in range(1,201):
        resultCode = generate200Keys.codeGenerator_byRandom()
        codeStr.append(resultCode)
        print ("%d: "%i + resultCode)
    test=save_keys_to_mysql('keys_text.txt')
#如果是在函数调用中,*args表示将可迭代对象扩展为函数的参数列表
#args=(1,2,3)
#func=(*args)
#等价于函数调用func(1,2,3)
#函数调用的**表示将字典扩展为关键字参数

    test.save_to_mysql(codeStr,**config)
    test.see_all(**config)
