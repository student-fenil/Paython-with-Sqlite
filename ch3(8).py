import sqlite3

conn = sqlite3.connect('college.db')
cur = conn.cursor()

# create table if not exists
cur.execute('''CREATE TABLE IF NOT EXISTS class (
                no INTEGER PRIMARY KEY,
                total_students INTEGER)''')

# take input from user
no = int(input("Enter class number: "))
stud = int(input("Enter total no. of students: "))

# insert if not exists, else update
cur.execute("SELECT * FROM class WHERE no=?", (no,))
row = cur.fetchone()

if row:
    cur.execute("UPDATE class SET total_students=? WHERE no=?", (stud, no))
else:
    cur.execute("INSERT INTO class (no, total_students) VALUES (?, ?)", (no, stud))

conn.commit()

# display all records
cur.execute("SELECT * FROM class")
rows = cur.fetchall()

print("\nClass No. | Total Students")
for r in rows:
    print(r[0], "       |", r[1])

conn.close()


'''
Enter class number: 1
Enter total no. of students: 3

Class No. | Total Students
1        | 3
'''