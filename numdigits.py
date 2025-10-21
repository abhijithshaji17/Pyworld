# Count the number of digits in given number()
a = int(input("Enter the number:"))
digits = 0
while (a>0):
    digits = digits + 1
    a = a//10
print ("a has", digits, "digits")