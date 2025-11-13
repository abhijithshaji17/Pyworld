'''
#Q5.
Write a Python program to input a string, count and print the vowels in it as capitals.
'''
vowels = ["a", "e", "i", "o", "u"]
msg = "Anuv Jain"
print (msg[0].upper()+msg[2].upper()+msg[6].upper()+msg[7].upper())
print (msg[0].upper()+msg[1]+msg[2].upper()+msg[3:5]+msg[5].lower()+msg[6].upper()+msg[7].upper()+msg[8])

for msg in vowels:
	v = 0
	if (msg in vowels):
	  v += 1
print (v)



