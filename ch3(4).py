import sqlite3

conn = sqlite3.connect("dbcollege.db")
print("Connected")

# Create table
conn.execute("""
CREATE TABLE IF NOT EXISTS tblclass (
    no INTEGER,
    name TEXT,
    ns INTEGER
)
""")

n = int(input("Enter number of records: "))

for i in range(n):
    print("Enter details for record", i + 1)

    no = int(input("Enter class no: "))
    name = input("Enter class name: ")
    ns = int(input("Enter total number of students: "))

    conn.execute(
        "INSERT INTO tblclass (no, name, ns) VALUES (?, ?, ?)",
        (no, name, ns)
    )

conn.commit()

print("Records inserted")

# Display records
c = conn.execute("SELECT * FROM tblclass")

for i in c:
    print("Class no:", i[0])
    print("Class name:", i[1])
    print("Total number of students:", i[2])

conn.close()