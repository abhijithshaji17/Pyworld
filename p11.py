'''
a) Write a python program to read date (entered by user) and is stored as a string in the format YYYY-MM-DD. You need to quickly extract only the year.

b) Display the year, month and date of the given date

c) Convert the string to tuple and display it.
'''
date = input("input the date in YYYY-MM-DD format: ")
print (date)
print (date.split ('-')[0])  # part a
date_parts = (date.split("-")) # part b
year = date_parts[0]
month = date_parts[1]
day = date_parts[2]
print ("Year:", year)
print ("Month:", month)
print ("Day:", day)
date_tuple = tuple(date_parts) # part c
print ("Date as tuple:", date_tuple)