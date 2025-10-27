# Pattern to print a pyramid with non repeated numbers
try:
    rows = int(input("Enter the number of rows: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Initialize the starting number
number = 1

print("\n--- Pyramid with Non-Repeating Numbers ---")

# Calculate the width needed for the last row
# This is tricky as numbers get wider (e.g., 9 vs 10)
# A simple spacing approach is used here.
# A more complex way would be to pre-calculate the max number's width.
# For simplicity, let's just use spaces based on row count.
k = rows - 1 # 'k' is the number of spaces

# Outer loop for each row
for i in range(1, rows + 1):
    
    # 1. Print leading spaces
    # Print 'k' spaces to center the content
    for space in range(k):
        print(end="  ") # Use two spaces for better visual balance
        
    # 2. Print the numbers for the current row
    for j in range(1, i + 1):
        
        # Print number, 'end=" "' keeps it on the same line
        # We use '{:<3}'.format(number) to give each number 
        # a fixed width (e.g., 3 spaces) for better alignment.
        # This prevents the triangle from skewing when 
        # numbers go from 1-digit (9) to 2-digits (10).
        
        print("{:<4}".format(number), end="")
        
        # Increment the non-repeating counter
        number += 1
        
    # 3. Move to the next line
    print()
    
    # 4. Decrement the space counter for the next row
    k -= 1