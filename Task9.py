# TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....

# Prompt the user for a number
rows = int(input("Enter a number: "))

# Print the stars in a triangular pattern
for i in range(1, rows + 1):
    print("*" * i)