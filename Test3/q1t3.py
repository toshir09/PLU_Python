roll_numbers = list(map(int, input("Enter roll numbers separated by space: ").split()))
search_roll = int(input("Enter the roll number to search: "))
found = False
for i in range(len(roll_numbers)):
    if roll_numbers[i] == search_roll:
        print("Student Found at position", i + 1)
        found = True
        break
if not found:
    print("Student Not Found.")