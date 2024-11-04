from datetime import datetime,date
# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
dob = input("Enter Date Of Birth yyyy/mm/dd: ")
dob_split = dob.split("-")
today = datetime.now()
today_month = today.month
today_year = today.year
today_day = today.day

years = today_year-int(dob_split[0])
months= today_month-int(dob_split[1])
days = today_day-int(dob_split[2])
print(f"{years} years,{months} months and {days} days")
