#Develop a Python program that categorizes a list of numbers into even and odd numbers using a single for loop and appends them to two separate lists. (Give sample input and output) 

numbers = [12, 7, 34, 23, 89, 4, 15]
even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)


print("Evens:", even_list)
print("Odds:", odd_list)
