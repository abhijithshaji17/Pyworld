# Kya Khaoge!!??
print("Kya Khaoge!!??")

try:
	choice = int(input("Enter the number corresponding to your choice: "))
except ValueError:
	print("Invalid input — please enter a number between 1 and 5.")
	choice = None

if choice == 1:
	print("Ghee roast, vada and chaya poi kazhikkam")
elif choice == 2:
	print("Poori, kadala curry and kaapi poi kazhikkam")
elif choice == 3:
	print("Idli, sambar and milk poi kazhikkam")
elif choice == 4:
	print("Porotta, vegetable stew and lemon tea poi kazhikkam")
elif choice == 5:
	print("Nothing, I'm on a diet onnum venda")
else:
	if choice is not None:
		print("Invalid choice — please select 1 through 5.")