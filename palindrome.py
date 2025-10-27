# Check whether a Number is Palindrome
n = int(input("Enter a Number:"))
temp = n
rev = 0
while (temp > 0):
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if (n == rev):
    print(n, "is a Palindromic number")  
else:
    print(n, "is not a Palindromic number")  