import sqlite3

# Connect to database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a table
cursor.execute("DROP TABLE IF EXISTS python_programming")
table = """ CREATE TABLE python_programming (
            id INT PRIMARY KEY,
            name TEXT NOT NULL,
            grade INT
        ); """
cursor.execute(table)

# Insert data into table
data = [(55, 'Carl Davis', 61),
       (66, 'Dennis Fredrickson', 88),
       (77, 'Jane Richards', 78),
       (12, 'Peyton Sawyer', 45),
       (2, 'Lucas Brooke', 99)]

cursor.executemany('INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)', data)

print("\nQuery 1......")
for row in cursor.execute("SELECT * FROM python_programming WHERE grade >= 60 and grade <= 80;"):
    print(row)

print("\nQuery 2......")
cursor.execute('UPDATE python_programming SET grade = 65 WHERE name="Carl Devis";')
for row in cursor.execute("SELECT * FROM python_programming;"):
    print(row)

print("\nQuery 3.......")
cursor.execute('DELETE FROM python_programming WHERE name="Denis Fredrickson";')
for row in cursor.execute("SELECT * FROM python_programming;"):
    print(row)

print("\nQuery 4.......")
cursor.execute('UPDATE python_programming SET grade = 10 WHERE id < 55;')
for row in cursor.execute("SELECT * FROM python_programming;"):
    print(row)


# Commit changes and close connection
conn.commit()
conn.close()
