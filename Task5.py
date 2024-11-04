# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

# Get three user inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Initialize a variable to hold the largest number
largest = num1

# Compare the second number with the current largest
if num2 > largest:
    largest = num2

# Compare the third number with the current largest
if num3 > largest:
    largest = num3

# Print the largest number
print("The largest number is:", largest)