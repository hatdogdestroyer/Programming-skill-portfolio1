# EXercise 5: Days of the Month

# This program tells you how many days are there in a specific month

# Mapping the month numbers to the number of days
days_of_the_month = {
    1: 31, # JANUARY
    2: 28, # FEBUARY
    3: 31, # MARCH
    4: 30, # APRIL
    5: 31, # MAY
    6: 30, # JUNE
    7: 31, # JULY
    8: 31, # AUGUST
    9: 30, # SEPTEMBER
    10: 31, # OCTOBER
    11: 30, # NOVEMBER
    12: 31, # DECEMBER
}

# Now you can ask the user for the month number
month_number = int(input("Enter the month number:"))

# Now you can check if the input exist
if 1 <= month_number <= 12:
    # Now Check if it's a leap year
    if month_number ==2:
        is_leap_year = input("Is it a lea[ year? (yes/no):").lower()
        if is_leap_year == "yes":
            print("Febuary has 29 days")
            days_of_the_month[2] = 29
        else:
            print("Febuary has 29 days")
            
            # Now you can print the number of days in the month
            print(f"There are {days_of_the_month[month_number]} days in month [month_number].")
else:
    print("Invalid month number. Please enter a number between1 and 12.")
    # This is a message when the number is not correct
                   

   
