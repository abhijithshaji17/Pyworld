# Pattern to print a right angle triangle with numbers non repeated
n = int(input("Enter a Number:"))   
i = 1
num = 1
while (i <= n): 
    j = 1
    while (j <= i):
        print(num, end=" ")
        num = num + 1
        j = j + 1
    print()
    i = i + 1