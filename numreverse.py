# Reverse of a Number
num  = int(input(("Enter the number:")))
reverse = 0
while (num>0):
    re = num % 10
    reverse = (reverse * 10) + re
    num = num // 10
print (reverse)