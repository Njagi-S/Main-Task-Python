# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

# Get the phone number from user input
phone_number = input("Enter phone number: ")

# Check if the phone number starts with +254, 07, 7, 01, or 1
if phone_number.startswith("+254"):
    if len(phone_number) == 13:  # Length should be 13
        pass  # No change needed
    else:
        print("Invalid phone number length for +254. It should be 13 characters.")
        exit()
elif phone_number.startswith("07"):
    if len(phone_number) == 10:  # Length should be 10
        phone_number = "+254" + phone_number[1:]  # Remove leading 0
    else:
        print("Invalid phone number length for 07. It should be 10 characters.")
        exit()
elif phone_number.startswith("7"):
    if len(phone_number) == 9:  # Length should be 9
        phone_number = "+254" + phone_number  # Keep as is
    else:
        print("Invalid phone number length for 7. It should be 9 characters.")
        exit()
elif phone_number.startswith("01"):
    if len(phone_number) == 10:  # Length should be 10
        phone_number = "+254" + phone_number[1:]  # Remove leading 0
    else:
        print("Invalid phone number length for 01. It should be 10 characters.")
        exit()
elif phone_number.startswith("1"):
    if len(phone_number) == 9:  # Length should be 9
        phone_number = "+254" + phone_number
    else:
        print("Invalid phone number length for 1. It should be 9 characters.")
        exit()
else:
    print("Invalid phone number")  # Invalid format
    exit()  # Exit the program

# Print the validated phone number
print("Valid phone number: " + phone_number)