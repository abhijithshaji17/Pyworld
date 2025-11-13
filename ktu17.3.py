#Predict output
for count in range(10, 0, -2):
   print (count, end = " ")

def greet_user():
	username = input("Enter name: ")
	greet = ("Hello" + username)
	return greet
print (greet_user()) 
print (greet_user()[::-1])

