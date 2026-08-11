# Write a code to input of class detail and insert the
# respective information into table tblclass


import sqlite3

# Connect database
conn = sqlite3.connect("dbcollege26.db")
print("Connected")

# Create table
conn.execute("""
CREATE TABLE IF NOT EXISTS tblclass (
    class_no INTEGER,
    class_name TEXT,
    total_students INTEGER
)
""")

# Input
no = int(input("Enter class no: "))
name = input("Enter class name: ")
ns = int(input("Enter total number of students: "))

# Insert record
conn.execute(
       "INSERT INTO tblclass (class_no, class_name, total_students) VALUES (?, ?, ?)",
    (no, name, ns)
)

conn.commit()

# Display records
c = conn.execute("SELECT * FROM tblclass")

for i in c:
    print("Class no:", i[0])
    print("Class name:", i[1])
    print("Total students:", i[2])

conn.close()