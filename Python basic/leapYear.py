year = int(input("Enter a year to be checked "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("{0} is a Leap year ".format(year))
else:
    print("{0} Not a Leap Year".format(year))
