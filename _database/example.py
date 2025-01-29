import sqlite3
import os

db_folder = "db"
if not os.path.exists(db_folder):
    os.makedirs(db_folder)

con = sqlite3.connect(f"{db_folder}/demodb.db")

con.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, major string)")
con.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY, name TEXT, major string, year INTEGER)")

# con.execute("DROP TABLE students_on_courses")
con.execute("CREATE TABLE students_on_courses (student_id INTEGER, course_id INTEGER, "
            "FOREIGN KEY (student_id) REFERENCES students(id), "
            "FOREIGN KEY (course_id) REFERENCES courses(id))")

# insert data
con.execute("INSERT INTO students (name, major) VALUES ('Serg',	'DS')")
con.execute("INSERT INTO students (name, major) VALUES ('Ann',	'DS')")
con.execute("INSERT INTO students (name, major) VALUES ('Min',	'DS')")
con.execute("INSERT INTO students (name, major) VALUES ('Alex',	'DS')")

# con.execute("DELETE FROM students WHERE id = 2")

# insert courses:
# PY1	CS	2024
# PY2	CS	2024
# PY3	CS	2025
# Data visuals	DS	2025
# Intro ML	DS	2024
# PY1	CS	2023

con.execute("INSERT INTO courses (name, major, year) VALUES ('PY1', 'CS', 2024)")
con.execute("INSERT INTO courses (name, major, year) VALUES ('PY2', 'CS', 2024)")
con.execute("INSERT INTO courses (name, major, year) VALUES ('PY3', 'CS', 2025)")
con.execute("INSERT INTO courses (name, major, year) VALUES ('Data visuals', 'DS', 2025)")
con.execute("INSERT INTO courses (name, major, year) VALUES ('Intro ML', 'DS', 2024)")
con.execute("INSERT INTO courses (name, major, year) VALUES ('PY1', 'CS', 2023)")

# con.execute("DELETE FROM students_on_courses")
#
con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (1, 4)")
con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (1, 3)")
con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (3, 1)")
con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (3, 2)")
con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (3, 3)")
con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (4, 1)")
con.execute("INSERT INTO students_on_courses (student_id, course_id) VALUES (5, 3)")
#
# # commit the transaction
con.commit()

# select data
cursor = con.execute("SELECT Name FROM students WHERE Name like '%a%'")
for row in cursor:
    print(row)


# select all student who took PY1 course in 2024
cursor = con.execute("SELECT s.* FROM students s "
                        "JOIN students_on_courses soc ON s.id = soc.student_id "
                        "JOIN courses c ON soc.course_id = c.id "
                        "WHERE c.name = 'PY1' AND c.year = 2024")
for row in cursor:
    print(row)