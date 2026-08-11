# Program to create table and to insert records

import sqlite3

conn = sqlite3.connect('dbcollege26.db')
print('Connected')

conn.execute('CREATE TABLE tblstudent (id int, name varchar(20))')
print('Table created')

conn.execute("INSERT INTO tblstudent VALUES (1,'Jinal')")

conn.execute("INSERT INTO tblstudent VALUES (2,'Fenil')")

conn.execute("INSERT INTO tblstudent VALUES (3,'Jenil')")

conn.execute('commit')
print('Record inserted')