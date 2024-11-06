# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
correct_password = "admin@123"
attempts = 0
max_attempts = 4

while attempts < max_attempts:
    password = input(f"Attempt {attempts + 1}: Please enter your password: ")

    if password == correct_password:
        print("Access granted!")
        break  # Exit the loop if the password is correct
    
    attempts += 1  # Increment the number of attempts
    print("Incorrect password. Please try again.You Have ", (max_attempts - attempts), "attempts left")


# Check if the maximum number of attempts has been reached
if attempts == max_attempts:
    print("Too many failed attempts. Your account is blocked.")