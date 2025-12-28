# Calculator

def add(x,y):
	return x+y
def subtract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	if y != 0:
		return x/y
	else:
		return "Error: division by zero"
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print("Operations:" "\n" "1. Addition\n2. Subtraction\n 3. Multiplication\n 4. Division")
choice = int(input("select the operation of your choice: "))
if choice == 1:
	print("The sum is: ", add(x,y))
elif choice == 2:
        print("The difference is: ", subtract(x,y))
elif choice == 3:
        print("The product is: ", multiply(x,y))
elif choice == 4:
        print("The remainder is: ", divide(x,y))
print("Over n out!")

