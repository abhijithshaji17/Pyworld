# Check whether given letter is a vowel or consonant
letter = input("Enter the character:")
if letter in ("a, e, i, o, u"):
    print(letter, "is a vowel")
else:
    print(letter, "is a consonant")