# Check for number divisible by 3 and 5
n = int(input("Enter a Number:"))
if (n % 3 == 0) and (n % 5 == 0):
    print(n, "is divisible by both 3 and 5")
else:
    print(n, "is not divisible by both 3 and 5")