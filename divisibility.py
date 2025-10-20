# Check for divisibility():
num1 = int(input(("Enter the first number:")))
num2 = int(input(("Enter the second number:")))
if num1 % num2 == 0:
    print(num1, "is divisible by", num2)
else:
    print(num1, "is not divisible by", num2)
