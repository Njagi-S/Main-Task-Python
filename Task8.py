# TASK 8: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70, it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.
# Prompt the user to input the speed of the car
speed = float(input("Enter the speed of the car (in km/h): "))

# Check if the speed is less than the speed limit
if speed < 70:
    print("Ok")
else:
    # Calculate the number of demerit points
    demerit_points = (speed - 70) // 5  # Integer division to get whole points

    # Print the total number of demerit points
    print(f"Demerit Points: {int(demerit_points)}")

    # Check if the license should be suspended
    if demerit_points > 12:
        print("License suspended!")