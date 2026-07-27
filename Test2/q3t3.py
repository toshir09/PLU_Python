n = int(input("Enter the number of students: "))
marks = []
print("Enter the marks:")
for i in range(n):
    marks.append(int(input()))
marks.sort()
print("Marks in ascending order:")
for mark in marks:
    print(mark, end=" ")