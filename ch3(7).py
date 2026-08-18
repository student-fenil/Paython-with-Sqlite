import sqlite3 as sq

# Connect to database and ensure the table exists
conn = sq.connect("dbcollege26.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS tblclass (
    class_no INTEGER,
    cname TEXT,
    total_students INTEGER
)
""")

# --- 1. Search & Display by Class Number ---
no = int(input("Enter class no: "))
cursor = conn.execute("SELECT * FROM tblclass WHERE class_no = ?", (no,))
records = cursor.fetchall()

print(f"\n--- Records with Class No: {no} ---")
if records:
    for i in records:
        print(f"Class No: {i[0]}, Class Name: {i[1]}, Total Students: {i[2]}")
else:
    print("No record found.")

# --- 2. Search & Display by Class Name ---
name = input("\nEnter class name: ")
cursor = conn.execute("SELECT * FROM tblclass WHERE cname = ?", (name,))
records = cursor.fetchall()

print(f"\n--- Records with Class Name: {name} ---")
if records:
    for i in records:
        print(f"Class No: {i[0]}, Class Name: {i[1]}, Total Students: {i[2]}")
else:
    print("No record found.")

# Close the database connection
conn.close()



'''
Enter class no: 1

--- Records with Class No: 1 ---
Class No: 1, Class Name: sybca, Total Students: 3
Class No: 1, Class Name: fybca, Total Students: 3

Enter class name: fybca

'''