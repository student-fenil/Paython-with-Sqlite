import sqlite3 as sq

# Connect database
conn = sq.connect('fenil.db')

# Create table if it does not exist
conn.execute('''
CREATE TABLE IF NOT EXISTS result (
    rollno INTEGER,
    sub1 INTEGER,
    sub2 INTEGER,
    sub3 INTEGER,
    sub4 INTEGER,
    sub5 INTEGER
)
''')

conn.commit()

# Insert record
j = int(input('if want to insert record type 1 otherwise 0: '))

if j == 1:

    n = int(input('how many records: '))

    i = 1

    while i <= n:

        a1 = int(input('enter roll no.: '))
        a2 = int(input('enter sub1 marks: '))
        a3 = int(input('enter sub2 marks: '))
        a4 = int(input('enter sub3 marks: '))
        a5 = int(input('enter sub4 marks: '))
        a6 = int(input('enter sub5 marks: '))

        conn.execute(
            f'INSERT INTO result VALUES ({a1},{a2},{a3},{a4},{a5},{a6})'
        )

        i = i + 1

# Select records
a = conn.execute('SELECT * FROM result')

conn.commit()

r = a.fetchall()

print('no sub1 sub2 sub3 sub4 sub5 total per')

for i in r:

    no = i[0]

    total = i[1] + i[2] + i[3] + i[4] + i[5]

    per = total / 5

    print(i[0], i[1], i[2], i[3], i[4], i[5], total, per)

conn.close()



'''
if want to insert record type 1 otherwise 0: 1
how many records: 1
enter roll no.: 2
enter sub1 marks: 33
enter sub2 marks: 44
enter sub3 marks: 55
enter sub4 marks: 66
enter sub5 marks: 77
no sub1 sub2 sub3 sub4 sub5 total per
2 33 44 55 66 77 275 55.0

if want to insert record type 1 otherwise 0: 0
no sub1 sub2 sub3 sub4 sub5 total per
2 33 44 55 66 77 275 55.0
'''