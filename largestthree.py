# Finding the Largest of Three Numbers
a = float(input("Enter a number:"))
b = float(input("Enter a number:"))
c = float(input("Enter a number:"))
largest = a
if (b > largest):
    largest = b
if (largest < c): 
    largest = c
print("The largest number is:", largest)
