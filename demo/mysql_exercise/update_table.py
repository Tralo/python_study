#!/usr/bin/env python
# coding=utf-8
import MySQLdb

db = MySQLdb.connect('localhost','root','123456','test')

cursor = db.cursor()

sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
            WHERE SEX = '%c'" % ('M')

try:
    cursor.execute(sql)

    db.commit()
except:
    db.rollback()
db.close()
