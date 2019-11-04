import sqlite3

with sqlite3.connect(".db") as db:
    cursor = db.cursor()

# Create Table

# Insert Data
db.commit()

db.close()
