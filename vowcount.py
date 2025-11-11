#Count vowels and check
vowels = ["a", "e", "i", "o", "u"]
ltr = input("Input a letter: ")
print (ltr in vowels)

x = input("Enter a string: ").lower()
s = 0
for i in x:
    if (i in vowels):
         s += 1
print (s)






