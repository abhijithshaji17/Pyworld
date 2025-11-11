#Menu driven calculator using conditions
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
input("Select operation of your choice: ")
choice = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n choice: "))
if choice == 1:
    print ("The sum is: ", x + y)
elif choice == 2:
    print ("The difference is: ", x - y)
elif choice == 3:
    print ("The product is: ", x * y)
elif choice == 4:
    if y != 0:
        print ("The quotient is: ", x / y)
    else:
        print("Error: Division by zero")
else: 
    print ("Invalid choice")
 
