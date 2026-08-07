import sqlite3 as sq

conn = sq.connect("fenil.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS emp(
    eid INTEGER,
    ename TEXT,
    salary INTEGER
)
""")

conn.execute("INSERT INTO emp VALUES(101,'fenil',5000)")
conn.commit()

r = conn.execute("SELECT * FROM emp")

for row in r:
    print(row)

conn.close()