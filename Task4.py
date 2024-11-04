# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

email = input("Please enter your email: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid Email!. Email should Have both the (@ and .) characters. Please Enter a Valid Email")
