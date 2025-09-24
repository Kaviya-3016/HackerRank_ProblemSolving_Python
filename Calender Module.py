# Import the calendar module which has functions to work with dates
import calendar

# Read a single line of input, split it by spaces, 
# convert each part to an integer, and assign to month, day, year
# Example input: "08 05 2015" -> month=8, day=5, year=2015
month, day, year = map(int, input().split())

# calendar.weekday(year, month, day) returns the day of the week as an integer
# 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
weekday_num = calendar.weekday(year, month, day)

# calendar.day_name is a list of weekday names: ['Monday', 'Tuesday', ...]
# Access the name corresponding to the weekday number
weekday_name = calendar.day_name[weekday_num]

# Print the weekday name in uppercase letters, as required by Hackerrank
print(weekday_name.upper())
