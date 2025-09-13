# Define a function called is_leap that takes 'year' as input
def is_leap(year):
    # By default, assume the year is not a leap year
    leap = False
    
    # Logic to check leap year:
    # Rule 1: If a year is divisible by 400, it is definitely a leap year
    if year % 400 == 0:
        leap = True
    
    # Rule 2: If a year is divisible by 4 but NOT divisible by 100,
    # then it is also a leap year
    elif year % 4 == 0 and year % 100 != 0:
        leap = True
    
    # Return the result (True if leap year, False otherwise)
    return leap


# ---- Main Program ----

# Take input from the user (always comes as string, so convert to int)
year = int(input())

# Call the function with the given year and print the result
print(is_leap(year))
