# Pattern to print a right angle triangle with numbers
n = int(input("Enter a Number:"))   
i = 1
while (i <= n): 
    j = 1
    while (j <= i):
        print(j, end=" ")
        j = j + 1
    print()
    i = i + 1
