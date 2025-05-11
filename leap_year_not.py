'''Q5. Write a program to calculate whether year is leap year or not?'''



# Input year from user
year = int(input("Enter a year: "))

# Leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
