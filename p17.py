#Discriminant of a quadratic equation ax^2 + bx + c is given by the formula D = b^2 - 4ac. Write a Python program to calculate the discriminant given the coefficients a, b, and c.
def find_discriminant(a, b, c):
    d = (b**2) - (4*a*c)
    print("Discriminant is:", d)

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

find_discriminant(a, b, c)