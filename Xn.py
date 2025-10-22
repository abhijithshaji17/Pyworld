# Power of a Number
base = float(input("Enter the base number:"))
power = float(input("Enter the power:"))
result = 1
i = 0
while (i < power):
    result = result * base
    i = i + 1   
print (base, "raised to the power", power, "is", result)