# Print multiplication table of given number
num = int(input("Enter the number: "))
for i in range(1, 11):
    print("Multiplication Table of", num, ":")
    print(f"{num} x {i} = {num * i}")
