'''
#Q3.
Write a program that takes a full name and forms a password using:

The first 3 letters of the first name

The last 3 letters of the last name

The total number of characters in the full name

append a special character @
'''
Name = "Donaldduck"
pass1 = (Name[0:3] + Name[7:10])
pass2 = "10"
pass3 = "@"
print (len(Name))
print ("Password is: ", pass1+pass2+pass3)

