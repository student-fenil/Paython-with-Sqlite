import sqlite3 as sq

# Connect to database (and create tblclass if it doesn't exist)
conn = sq.connect("dbcollege26.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS tblclass (
    class_no INTEGER,
    class_name TEXT,
    total_students INTEGER
)
""")

# User input
no = int(input("Enter class no: "))
name = input("Enter class name: ")
ns = int(input("Enter total number of students: "))

# Insert record using parameterized query (prevents syntax/SQL errors)
conn.execute("INSERT INTO tblclass VALUES (?, ?, ?)", (no, name, ns))
conn.commit()

# Fetch and display records
a = conn.execute("SELECT * FROM tblclass")
r = a.fetchall()

for i in r:
    print("class no:", i[0])
    print("class name:", i[1])
    print("no of students:", i[2])

# Close connection
conn.close()




'''
Enter class no: 1
Enter class name: sybca
Enter total number of students: 3
class no: 101
class name: div-2
no of students: 10
class no: 1
class name: sybca
no of students: 3
'''