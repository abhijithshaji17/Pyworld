'''
Perform the following task on list

a) Create list containing vowels

b) Write a python program to input an alphabet and check whether it is vowel or consonant

c) Print all the vowel in one by one
'''
vowels = ["a", "e", "i", "o", "u"]
print (vowels)
ltr = input("Input a letter: ")
if (ltr in vowels):
    print (ltr, "is a vowel")
else:
    print (ltr, "is a consonant")

x = input("Enter a string: ").lower()
s = 0
for i in x:
    if (i in vowels):
         s += 1
print (s)

