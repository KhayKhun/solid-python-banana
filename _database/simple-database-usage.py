import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

db_path = os.path.join(db_folder, "library.db")
con = sqlite3.connect(db_path)

# Create tables
# con.execute("""
#     CREATE TABLE authors (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     )
# """)
# con.execute("""
#     CREATE TABLE publishers (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     )
# """)

# con.execute("""
#     CREATE TABLE books (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         author_id INTEGER NOT NULL,
#         publisher_id INTEGER NOT NULL,
#         FOREIGN KEY (author_id) REFERENCES authors(id),
#         FOREIGN KEY (publisher_id) REFERENCES publishers(id)
#     )
# """)

authors = ["Sai", "Chill Guy", "Pency"]

publishers = ["Bangkok Publishing", "Oxford", "Cool company"]

books = [
    ("1984", 1, 1),
    ("Animal Farm", 1, 2),
    ("It Rains but it doesn't pour", 2, 3),
    ("Emma", 2, 2),
    ("Adventures of Tom Sawyer", 3, 1)
]

# Insert data
# for a in authors:
#     con.execute(f"INSERT INTO authors (name) VALUES ('{a}')")
# for p in publishers:
#     con.execute(f"INSERT INTO publishers (name) VALUES ('{p}')")
# for b in books:
#     con.execute("INSERT INTO books (title, author_id, publisher_id) VALUES (?, ?, ?)",(b[0], b[1], b[2]))
# con.commit()


print("=== All authors ===")
cursor = con.execute("SELECT * FROM authors")
for row in cursor:
    print(row)

print("=== All publishers ===")
cursor = con.execute("SELECT * FROM publishers")
for row in cursor:
    print(row)

print("=== All books ===")
cursor = con.execute("""
    SELECT b.title, a.name AS author_name, p.name AS publisher_name
    FROM books b
    JOIN authors a ON b.author_id = a.id
    JOIN publishers p ON b.publisher_id = p.id
""")
for row in cursor:
    print(row)

con.close()