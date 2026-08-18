import sqlite3 as sq

# Connect to database and create sample table if it does not exist
conn = sq.connect("fenil.db")
conn.execute("""
CREATE TABLE IF NOT EXISTS tblstud_result (
    rno INTEGER PRIMARY KEY,
    s1 INTEGER,
    s2 INTEGER,
    s3 INTEGER,
    s4 INTEGER,
    s5 INTEGER
)
""")

# Input cutoff marks from user
min_marks = int(input("Enter minimum marks: "))

# Fetch records where BOTH Subject 1 and Subject 2 are greater than entered marks
cursor = conn.execute(
    "SELECT * FROM tblstud_result WHERE s1 > ? AND s2 > ?", 
    (min_marks, min_marks)
)
records = cursor.fetchall()

# Display matching records
if records:
    print("\n--- Matching Student Records ---")
    print(f"{'Roll No':<10}{'S1':<6}{'S2':<6}{'S3':<6}{'S4':<6}{'S5':<6}")
    print("-" * 40)
    for row in records:
        print(f"{row[0]:<10}{row[1]:<6}{row[2]:<6}{row[3]:<6}{row[4]:<6}{row[5]:<6}")
else:
    print("\nNot enough marks / No records found matching the criteria.")

# Close connection
conn.close()



'''
Enter minimum marks: 80

Not enough marks / No records found matching the criteria.

'''