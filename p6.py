#palindrome

def palindrome_check(a):
	if a == a[::-1]:
		print(a, "is palindrome")
	else:
		print(a, "is not palindrome")

a = input("Enter something: ")
palindrome_check(a)
