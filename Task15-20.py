# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:

# Function to calculate the gross_salary;
def calculateGrossSalary(basic_sal, bens):
    gross = basic_sal + bens
    return gross

basicSalary = float(input("Enter Your Basic Salary: "))
benefits = float(input("Enter Your Benefits: "))
gross_salary = calculateGrossSalary(basicSalary, benefits)
print(f"Your Gross Salary is: {gross_salary}")

# Function to calculate NHIF
def calculateNHIF(sal_range):
    deductions = 0
    if sal_range >= 0 and sal_range <= 5_999:
        deductions = 150
    elif sal_range >= 6_000 and sal_range <= 7_999:
        deductions = 300
    elif sal_range >= 8_000 and sal_range <= 11_999:
        deductions = 400
    elif sal_range >= 12_000 and sal_range <= 14_999:
        deductions = 500
    elif sal_range >= 15_000 and sal_range <= 19_999:
        deductions = 600
    elif sal_range >= 20_000 and sal_range <= 24_999:
        deductions = 750
    elif sal_range >= 25_000 and sal_range <= 29_999:
        deductions = 850
    elif sal_range >= 30_000 and sal_range <= 34_999:
        deductions = 900
    elif sal_range >= 35_000 and sal_range <= 39_999:
        deductions = 950
    elif sal_range >= 40_000 and sal_range <= 44_999:
        deductions = 1000
    elif sal_range >= 45_000 and sal_range <= 49_999:
        deductions = 1100
    elif sal_range >= 50_000 and sal_range <= 59_999:
        deductions = 1200
    elif sal_range >= 60_000 and sal_range <= 69_999:
        deductions = 1300
    elif sal_range >= 70_000 and sal_range <= 79_999:
        deductions = 1400
    elif sal_range >= 80_000 and sal_range <= 89_999:
        deductions = 1500
    elif sal_range >= 90_000 and sal_range <= 99_999:
        deductions = 1600
    else:
        deductions = 1700

    return deductions

NHIF = calculateNHIF(gross_salary)
print(f"Your NHIF Deductions is: {NHIF}")


# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use the gross salary to find the NSSF.
# To find the Kenya NSSF Rate using 6% of the Gross Salary.
# BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF.


# Function to calculate nssf
def calculate_nssf(nssf1):
    nssf2 = 0
    if nssf1 >= 0 and nssf1 <= 18000:
        nssf2 = 0.06 * nssf1        
    else:
        nssf2 = 0.06 * 18000
    return nssf2
NSSF = calculate_nssf(gross_salary)
print(f"Your NSSF Contribution is: {NSSF}")


# Task 17: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s NHDF using:
# i.e NHDF = gross_salary * 0.015

def calculate_nhdf(pay):
    NHDF9 = gross_salary * 0.015
    return NHDF9

NHDF = calculate_nhdf(gross_salary)
print(f"Your NHDF Contribution is: {NHDF}")