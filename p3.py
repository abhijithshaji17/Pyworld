# Write a program using a loop that calculates the factorial of a user-defined number N (e.g., if N=5, the result is 5 X 4 X3 X2 1=120). Assume N is a positive integer.

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter a number: "))
print(fact(n))