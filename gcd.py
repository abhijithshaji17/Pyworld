# GCD of 2 numbers
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
while(b != 0):
    temp = b
    b = a % b
    a = temp
print("GCD is:", a)


