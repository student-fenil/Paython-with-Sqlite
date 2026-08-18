import sqlite3

conn = sqlite3.connect('database.db')

print('Connected')

conn.execute('CREATE TABLE IF NOT EXISTS tblstud (id INT, name VARCHAR(70))')

print('Table created')

conn.execute("INSERT INTO tblstud VALUES (3, 'Fenil')")

conn.commit()

print('Record inserted')



'''
Connected
Table created
Record inserted
'''