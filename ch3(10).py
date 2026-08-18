# create tbldept (dno int, dname)
# and tblstud (rno, name, per, dno)

# assign primary as well as
# foreign key

import sqlite3

conn = sqlite3.connect("fenil.db")

conn.execute("PRAGMA foreign_keys = ON")

conn.execute("""
DROP TABLE IF EXISTS tblstud
""")

conn.execute("""
DROP TABLE IF EXISTS tbldept
""")

conn.execute("""
CREATE TABLE tbldept(
    dno INTEGER PRIMARY KEY,
    dname VARCHAR(20)
)
""")

conn.execute("""
INSERT INTO tbldept VALUES(1, 'BCA')
""")

conn.execute("""
CREATE TABLE tblstud(
    rno INTEGER PRIMARY KEY,
    name VARCHAR(70),
    per INTEGER,
    dno INTEGER,
    FOREIGN KEY(dno) REFERENCES tbldept(dno)
)
""")

conn.execute("""
INSERT INTO tblstud VALUES(1, 'fenil', 70, 1)
""")

conn.commit()

print("Table created and data inserted successfully.")

conn.close()