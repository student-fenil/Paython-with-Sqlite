import sqlite3

conn = sqlite3.connect('dbcollege26.db')

no = int(input('Enter class no: '))

a = conn.execute(
    'SELECT * FROM tblclass WHERE cno=?',
    (no,)
)

x = c.fetchall()

for i in x:
    print(i[0], i[1], i[2])


name = input('Enter class name: ')

c = con.execute(
    'SELECT * FROM tblclass WHERE cname=?',
    (name,)
)

x = c.fetchall()

for i in x:
    print(i[0], i[1], i[2])