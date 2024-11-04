# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
# Prompt the user for four numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Initialize the largest number with the first input
largest = num1

# Compare with the second number
if num2 > largest:
    largest = num2

# Compare with the third number
if num3 > largest:
    largest = num3

# Compare with the fourth number
if num4 > largest:
    largest = num4

# Print the largest number
print("The largest number is:", largest)