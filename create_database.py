import sqlite3

conn = sqlite3.connect("datasets/company.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    age INTEGER
)
""")

employees = [
    (1, "Alice", "HR", 45000, 25),
    (2, "Bob", "IT", 60000, 30),
    (3, "Charlie", "Finance", 55000, 29),
    (4, "David", "IT", 70000, 35),
    (5, "Eva", "Marketing", 48000, 27),
    (6, "Frank", "Finance", 65000, 32),
    (7, "Grace", "HR", 52000, 28),
    (8, "Henry", "IT", 75000, 40),
    (9, "Ivy", "Sales", 43000, 24),
    (10, "Jack", "Marketing", 58000, 31)
]

cursor.executemany(
    "INSERT INTO employees VALUES (?, ?, ?, ?, ?)",
    employees
)

conn.commit()
conn.close()

print("Database created successfully!")
