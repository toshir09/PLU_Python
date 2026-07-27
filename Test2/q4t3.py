n = int(input("Enter the number of participants: "))
timings = []
print("Enter the timings (in seconds):")
for i in range(n):
    timings.append(float(input()))
timings.sort()
print("Ranked Timings (Fastest to Slowest):")
for time in timings:
    print(time, end=" ")