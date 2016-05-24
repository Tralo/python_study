#!/usr/bin/env python
# coding=utf-8
import MySQLdb

def writeToMysql():
    file = open("codes.txt","rU")
    # 获取文件行数
    contents = file.readlines()
    count = len(contents)
    print "文件行数: '%d'" % count

    

    #写入数据库
    db = MySQLdb.connect('localhost','root','123456','test')
    cursor = db.cursor()
    
    #创建表格
    create_table(cursor)
    
    # 写入表格中
    index = 1;
    for line in contents:
        
        print "写入第'%d'条数据: %s" % (index,line)
        insert(db,cursor,line)
        index = index + 1
    db.close()
    file.close()

def create_table(cursor):

    cursor.execute("DROP TABLE IF EXISTS CODE_KEY")
    sql = """CREATE TABLE CODE_KEY (
        KEY_CODE CHAR(30) NOT NULL   
    )"""
    cursor.execute(sql)

def insert(db,cursor,line):
    sql = "INSERT INTO CODE_KEY (KEY_CODE) VALUES ('%s')" % line
    cursor.execute(sql)
    db.commit()



if __name__ == "__main__":
    writeToMysql()


