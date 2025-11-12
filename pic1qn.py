# (a) Read a string from the user.
original_string = input("Enter a string: ")

# (b) Remove all spaces and count the number of characters in the string.
string_without_spaces = original_string.replace(" ", "")
char_count = len(string_without_spaces)
print(f"String without spaces: {string_without_spaces}")
print(f"Number of characters (excluding spaces): {char_count}")

# (c) Replace all vowels in the string with the "#" symbol.
vowels = "aeiouAEIOU"
string_with_vowels_replaced = ""
for char in original_string:
    if char in vowels:
        string_with_vowels_replaced += "#"
    else:
        string_with_vowels_replaced += char
print(f"String with vowels replaced: {string_with_vowels_replaced}")

# (d) Reverse the string and display it.
reversed_string = original_string[::-1]
print(f"Reversed string: {reversed_string}")
