#!/usr/bin/env python
# coding=utf-8
import MySQLdb

db = MySQLdb.connect('localhost','root','123456','test')

cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:

    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
