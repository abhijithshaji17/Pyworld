# Triangle combo
n = int(input("Enter a Number:"))
i = 0           
j = 0
# Right Angled Triangle
while (i < n):
    j = 0
    while (j <= i):
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1
# Inverted Right Angled Triangle
# Start from n-1 so the shared middle line isn't duplicated, then decrease to 1
i = n - 1
while (i > 0):
    j = 0
    # print exactly i stars on this row
    while (j < i):
        print("*", end=" ")
        j = j + 1
    print()
    i = i - 1