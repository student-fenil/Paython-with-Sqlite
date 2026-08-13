import sqlite3

conn = sqlite3.connect('stud.db')
cur = conn.cursor()

# create table if not exists (so delete/select don't fail on a fresh db)
cur.execute('''CREATE TABLE IF NOT EXISTS tblclass (
                name TEXT,
                total_students INTEGER)''')

name = input("Enter class name: ")

cur.execute("DELETE FROM tblclass WHERE name=?", (name,))
conn.commit()

r = cur.execute("SELECT * FROM tblclass").fetchall()
for i in r:
    print(i[0], i[1])

conn.close()