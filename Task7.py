# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

# Prompt the user to input student marks
marks = float(input("Please enter student marks (0-100): "))

# Check if the input is within the valid range
if 0 <= marks <= 100:
    # Determine the grade based on the marks
    if marks > 79:
        grade = "A"
    elif 60 <= marks <= 79:
        grade = "B"
    elif 50 <= marks <= 59:
        grade = "C"
    elif 40 <= marks <= 49:
        grade = "D"
    else:
        grade = "E"
    
    # Print the grade
    print(f"The grade is: {grade}")
else:
    print("Invalid input! Marks should be between 0 and 100.")