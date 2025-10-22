# Sum of all odd terms in a group of n numbers
n = int(input("Enter the number of terms: "))
sum_odd = 0
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 != 0:
        sum_odd += num
print(f"The sum of all odd terms is: {sum_odd}")    