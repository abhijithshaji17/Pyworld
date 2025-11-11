# Leap Year Checker
y = int(input("Enter a Year:"))
if (y % 4 == 0):
    if (y % 100 == 0):
        if (y % 400 == 0):
            print (y, "is a Leap Year")
        else:
            print (y, "is not a Leap Year")
    else: 
        print (y, "is a Leap Year")
else:
    print (y, "is not a Leap Year")