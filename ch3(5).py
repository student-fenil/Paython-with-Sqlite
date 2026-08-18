import sqlite3

# Connect to database and ensure table exists
conn = sqlite3.connect("dbcollege26.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS tblclass (
    class_no INTEGER,
    class_name TEXT,
    total_students INTEGER
)
""")

# Input number of records to add
n = int(input("Enter number of records: "))

# Loop to insert records
for i in range(n):
    print(f"\nEnter details for record {i + 1}:")
    no = int(input("Enter class no: "))
    name = input("Enter class name: ")
    ns = int(input("Enter total number of students: "))
    
    # Insert record into tblclass
    conn.execute("INSERT INTO tblclass VALUES (?, ?, ?)", (no, name, ns))

# Save changes
conn.commit()

# Display all records
print("\n--- All Records in tblclass ---")
cursor = conn.execute("SELECT * FROM tblclass")
records = cursor.fetchall()

for row in records:
    print(f"Class No: {row[0]}, Class Name: {row[1]}, Total Students: {row[2]}")

# Close database connection
conn.close()



'''
Enter number of records: 1

Enter details for record 1:
Enter class no: 1
Enter class name: fybca
Enter total number of students: 3

--- All Records in tblclass ---
Class No: 101, Class Name: div-2, Total Students: 10
Class No: 1, Class Name: sybca, Total Students: 3
Class No: 1, Class Name: fybca, Total Students: 3
'''