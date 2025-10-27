# Loop until right password "python123" is entered
while True:
    password = input("Enter the password: ")
    if (password == "python123"):
        print("Access granted!")
        break
    else:
        print("Incorrect password, try again.") 