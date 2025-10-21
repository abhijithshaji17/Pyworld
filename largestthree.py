# Finding the Largest of Three Numbers
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
largest = a
if (b > largest):
    largest = b
if (largest < c): 
    largest = c
print("The largest number is:", largest)
