import sqlite3

# Connect to database
conn = sqlite3.connect("dbcollege26.db")
cursor = conn.cursor()

# Drop existing table if needed and create new table
cursor.execute("DROP TABLE IF EXISTS tblstud_result")
cursor.execute("""
    CREATE TABLE tblstud_result (
        rno INTEGER PRIMARY KEY,
        s1 INTEGER,
        s2 INTEGER,
        s3 INTEGER,
        s4 INTEGER,
        s5 INTEGER
    )
""")

# Insert student marks
cursor.execute("INSERT INTO tblstud_result VALUES (101, 80, 75, 66, 70, 75)")
cursor.execute("INSERT INTO tblstud_result VALUES (102, 71, 74, 61, 74, 90)")
conn.commit()

# Add new column 'grade'
cursor.execute("ALTER TABLE tblstud_result ADD COLUMN grade TEXT")
conn.commit()

# Fetch records to calculate percentage and grade
cursor.execute("SELECT * FROM tblstud_result")
records = cursor.fetchall()

for row in records:
    rno = row[0]
    total = row[1] + row[2] + row[3] + row[4] + row[5]
    per = total / 5.0

    # Determine Grade
    if per >= 70:
        grade = "Distinction"
    elif per >= 60:
        grade = "First"
    elif per >= 50:
        grade = "Second"
    elif per >= 35:
        grade = "Pass"
    else:
        grade = "Fail"

    # Update grade for this specific student
    cursor.execute(
        "UPDATE tblstud_result SET grade = ? WHERE rno = ?",
        (grade, rno)
    )

conn.commit()

# Display all updated records
print(f"{'Roll No':<10}{'S1':<6}{'S2':<6}{'S3':<6}{'S4':<6}{'S5':<6}{'Grade':<12}")
print("-" * 50)

cursor.execute("SELECT * FROM tblstud_result")
for row in cursor.fetchall():
    print(f"{row[0]:<10}{row[1]:<6}{row[2]:<6}{row[3]:<6}{row[4]:<6}{row[5]:<6}{row[6]:<12}")

conn.close()




'''
Roll No   S1    S2    S3    S4    S5    Grade       
--------------------------------------------------
101       80    75    66    70    75    Distinction 
102       71    74    61    74    90    Distinction 

'''