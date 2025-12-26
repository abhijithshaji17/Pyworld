'''
Write a python program to display the shipping fee. Shipping fee is calculate based on the following criteria:
Read the weight of the parcel from the user
Fee is $5 if weight <=1.
Fee is $10 if weight <= 5.
Fee is $20 otherwise.
'''

def shipping_fee():
	if weight <=1:
	  return "$5"
	elif weight <= 5:
          return "$10"
	else:
	  return "$20"
weight = float(input("Enter your parcel's weight in kg: "))
print ("shipping fee is: ", shipping_fee())

