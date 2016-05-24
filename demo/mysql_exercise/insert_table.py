#!/usr/bin/env python
# coding=utf-8
import MySQLdb

db = MySQLdb.connect('localhost','root','123456','test')

cursor = db.cursor()

sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
        LAST_NAME,AGE,SEX,INCOME) \
        VALUES ('%s','%s','%d','%c','%d')" % \
        ('Mac', 'Mohan', 20, 'M', 2000)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
