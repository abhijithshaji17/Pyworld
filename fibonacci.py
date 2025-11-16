#Fibonacci Series
a = 0
b = 1
n = int(input("Enter the number of terms: "))
print("Fibonacci Series:")
for i in range(n):
    print(a, end=' ')
    next_term = a + b
    a = b
    b = next_term