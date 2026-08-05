# # 4. College Placement Portal
# ### Problem Statement
# A college stores student records in SQLite.
# Each student contains:
# * Roll Number
# * Name
# * CGPA
# * Skills
# * Placement Status
# ### Requirements
# 1. Retrieve all students.
# 2. Sort students by CGPA using **Heap Sort**.
# 3. Search students by Roll Number.
# 4. Display students eligible for placements (CGPA > 7.5).
# 5. Update placement status after selection.
# ### Concepts
# * Heap
# * Heap Sort
# * Binary Search
# * SQL UPDATE
import sqlite3
# Student Class
class Student:
    def __init__(self, roll_no, name, cgpa, skills, status):
        self.roll_no = roll_no
        self.name = name
        self.cgpa = cgpa
        self.skills = skills
        self.status = status
    def display(self):
        print("-" * 45)
        print("Roll Number      :", self.roll_no)
        print("Name             :", self.name)
        print("CGPA             :", self.cgpa)
        print("Skills           :", self.skills)
        print("Placement Status :", self.status)
# Create SQLite Database
conn = sqlite3.connect("placement.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll_no INTEGER PRIMARY KEY,
    name TEXT,
    cgpa REAL,
    skills TEXT,
    status TEXT
)
""")
# Remove old data
cursor.execute("DELETE FROM students")
students_data = [
    (101, "Rahul", 8.5, "Python, SQL", "Not Placed"),
    (102, "Priya", 9.2, "Java, C++", "Not Placed"),
    (103, "Amit", 7.1, "Python", "Not Placed"),
    (104, "Sneha", 8.8, "Java, Python", "Not Placed"),
    (105, "Ravi", 6.9, "C", "Not Placed"),
    (106, "Neha", 7.8, "SQL, Python", "Not Placed"),
    (107, "Kiran", 9.5, "AI, ML", "Not Placed"),
    (108, "Pooja", 7.3, "HTML, CSS", "Not Placed")
]
cursor.executemany("INSERT INTO students VALUES(?,?,?,?,?)", students_data)
conn.commit()
# Fetch Students
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
students = []
for row in rows:
    students.append(Student(*row))
# Heap Sort Functions
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left].cgpa > arr[largest].cgpa:
        largest = left
    if right < n and arr[right].cgpa > arr[largest].cgpa:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
heap_sort(students)
print("\nStudents Sorted by CGPA\n")
for student in students:
    student.display()
# Binary Search
students.sort(key=lambda x: x.roll_no)
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].roll_no == key:
            return arr[mid]
        elif arr[mid].roll_no < key:
            low = mid + 1
        else:
            high = mid - 1
    return None
roll = int(input("\nEnter Roll Number to Search: "))
result = binary_search(students, roll)
if result:
    print("\nStudent Found")
    result.display()
else:
    print("\nStudent Not Found")
# Eligible Students
print("\nStudents Eligible for Placement (CGPA > 7.5)\n")
eligible = []
for student in students:
    if student.cgpa > 7.5:
        student.display()
        eligible.append(student)
# Update Placement Status
roll = int(input("\nEnter Roll Number to Mark as Placed: "))
cursor.execute(
    "UPDATE students SET status='Placed' WHERE roll_no=?",
    (roll,)
)
conn.commit()
print("\nUpdated Student Details\n")
cursor.execute("SELECT * FROM students WHERE roll_no=?", (roll,))
row = cursor.fetchone()
if row:
    Student(*row).display()
else:
    print("Student Not Found")
conn.close()