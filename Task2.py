# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
# Hint: how does an even / odd number react differently when divided by 2?
number =  int(input("Enter a number: "))
if number % 2 == 0:
    print("The Number is even")
else:
    print("The Number is odd")


# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
if number % 4 == 0:
    print("The Number is divisible by 4")
else:
    print("The Number is not  divisible by 4")

