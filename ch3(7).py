import sqlite3

conn = sqlite3.connect('dbcollege26.db')

no = int(input('Enter marks: '))

c = conn.execute(
    'SELECT * FROM tblstudent WHERE s1 > ?',
    (no,)
)

x = c.fetchall()

for i in x:
    print(i[0], i[1], i[2], i[3], i[4], i[5])

conn.close()