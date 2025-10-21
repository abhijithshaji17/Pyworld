# Inverted Right Angled Triangle
n = int(input("Enter a Number:"))
i = n
j = 0
while (i > 0):
    j = 0
    while (j < i):
        print("*", end=" ")
        j = j + 1
    print()
    i = i - 1  
