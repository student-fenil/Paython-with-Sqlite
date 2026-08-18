import sqlite3

conn = sqlite3.connect("dbguide26.db")

no = int(input("Enter roll no: "))
nm = input("Enter stud name: ")

conn.execute(
    "INSERT INTO tblstud VALUES (?, ?)",
    (no, nm)
)

conn.commit()

c = conn.execute("SELECT * FROM tblstud")

for i in c:
    print("Roll no:", i[0])
    print("Name:", i[1])

conn.close()