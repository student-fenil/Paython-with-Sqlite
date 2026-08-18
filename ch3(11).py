# display students detail
# with department name

# create tbldept (dno, dname)
# and tblstud (rno, name, per, dno)


import sqlite3

conn = sqlite3.connect("dbserver26.db")

# Create department table
conn.execute("""
CREATE TABLE IF NOT EXISTS tbldept(
    dno INTEGER PRIMARY KEY,
    dname VARCHAR(20)
)
""")

# Insert department
conn.execute("""
INSERT OR IGNORE INTO tbldept VALUES(1, 'BCA')
""")

# Create student table
conn.execute("""
CREATE TABLE IF NOT EXISTS tblstud(
    rno INTEGER PRIMARY KEY,
    name VARCHAR(70),
    per INTEGER,
    dno INTEGER,
    FOREIGN KEY(dno) REFERENCES tbldept(dno)
)
""")

# Insert student
conn.execute("""
INSERT OR IGNORE INTO tblstud VALUES(1, 'fenil', 70, 1)
""")

# Display students detail with department name
c = conn.execute("""
SELECT a.*, b.dname
FROM tblstud a
JOIN tbldept b ON a.dno = b.dno
""")

r = c.fetchall()

for i in r:
    print(i)

conn.commit()
