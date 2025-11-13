'''
#Q1.
Write a Python program to generate a password using the user's name and date of birth in the format DD-MM-YYYY.

The password should follow these rules:

Take the first three letters of the name (in uppercase).

Take the last two digits of the birth year.

Take the sum of the digits in the day part of the DOB.

Combine all the above and append a special character @

Enter your full name: Gautham Sankar

Enter your DOB (DD-MM-YYYY): 15-07-2002

GAUQ26@
'''
Name = "Nandini Srikar"
DOB = "11-09-2003"
a = Name[0:3].upper()
b = "03"
s = "2"
d = "%"
print (a)
print (DOB[8:10])
print (DOB[0]+DOB[1])
print (a+b+s+d)
 
