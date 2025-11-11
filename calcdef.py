#Menu driven calculator with function
def add(x,y):
   return x + y
def subtract(x,y):
   return x - y
def product(x,y):
   return x * y
def division(x,y):
   if y != 0:
         return x / y
   else: 
         return "Error: Division by zero"
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
print ("Select the operation of your choice: ")
print ("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = int(input("Select your choice: "))
if choice == 1:
    print ("The sum is: ", add(x,y))
elif choice == 2:
    print ("The differnce is: ", subtract(x,y))
elif choice == 3:
    print ("The product is: ", product(x,y))
elif choice == 4:
    print ("The quotient is: ", division(x,y))
print ("Over n Out!")

