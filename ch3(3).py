import sqlite3

# Connect database
conn = sqlite3.connect("dbcollege.db")
print("Connected")

# Create table
conn.execute("""
CREATE TABLE IF NOT EXISTS tblstd (
    rno INTEGER,
    name TEXT
)
""")

print("Table created")

# Insert record
conn.execute(
    "INSERT INTO tblstd (rno, name) VALUES (?, ?)",
    (1, "Jinal")
)

# Save changes
conn.commit()

print("Record inserted")

# Close connection
conn.close()