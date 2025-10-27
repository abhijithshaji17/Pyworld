# Finding Factorial of a Number
n = int(input("Enter a Number:"))
fact = 1
i = 1
while (i <= n):
    fact = fact * i
    i = i + 1
print("Factorial of", n, "is", fact)