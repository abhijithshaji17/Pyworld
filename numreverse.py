# Reverse of a Number
num  = int(input(("Enter the number:")))
reverse = 0
while (num>0):
    reverse = reverse + num%10
    reverse = reverse*10
    num = num//10
print (reverse)