import sqlite3 as sq

# Connect to database and ensure the table exists
conn = sq.connect("fenil.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tblclass (
    class_no INTEGER PRIMARY KEY,
    class_name TEXT,
    no_stud INTEGER
)
""")

# Take user input
no = int(input("Enter class number: "))
no_stud = int(input("Enter total number of students: "))

# Update the record using parameterized query
cursor.execute(
    "UPDATE tblclass SET no_stud = ? WHERE class_no = ?",
    (no_stud, no)
)
conn.commit()

# Check if any row was actually updated
if cursor.rowcount > 0:
    print(f"\nRecord successfully updated for class number: {no}")
else:
    print(f"\nNo record found with class number: {no}")

# Display updated records to verify
print("\n--- Current tblclass Records ---")
cursor.execute("SELECT * FROM tblclass")
for row in cursor.fetchall():
    print(row)

# Close the database connection
conn.close()



'''
Enter class number: 1
Enter total number of students: 3

No record found with class number: 1

--- Current tblclass Records ---

'''