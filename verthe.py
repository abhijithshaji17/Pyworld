#Test
def newline():
   print()
for count in range(5, 0, -1):
    print(count, end = " ")
newline()
newline()
def factorial(n): 
    if n == 0:
      return 1
    else:
      return n * factorial(n-1)
n = int(input("Enter a number: "))
print ('Factorial of', n, 'is', factorial(n))
