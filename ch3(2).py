#Write a Python program to fetch a single record from an SQLite table and display the data.


import sqlite3

conn = sqlite3.connect('dbcollege26.db')
a =conn.execute('select * from tblstud')

b = a.fetchone()
print(b)

b = a.fetchone()
print(b)

print('demantion wise')
print('roll no:', b[0])
print('name:', b[1])

b = a.fetchone()
print('Rollno:', b[0])
print('name:', b[1])