#Calculates your age in days by entering birthday and current date.
#Inputs: Two dates
#Valid inputs:
##Second date must not be before first data - 1
##Gregorian Calender (15 Oct 1582) - 2
#Representation of Inputs

def isLeapYear(year):
##    if (year is not divisible by 4) then (it is a common year)
##else if (year is not divisible by 100) then (it is a leap year)
##else if (year is not divisible by 400) then (it is a common year)
##else (it is a leap year)

    if ((year%4 == 0) or (year%400 == 0)):
        return True
    elif (year%100 == 0):
        return False
    return False

#No. of days every month
def daysInMonth(year, month):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        if ((month == 2) and (isLeapYear(year))):
            return 29
        elif (month == 2):
            return 28
        else:
            return 30
    return 30

#Computes next day
def nextDay(year, month, day):
    #Assuming each month having 30 days
    if (day < daysInMonth(year, month)):
        return year, month, day + 1
    else:
        if (month < 12):
            return year, month + 1, 1
        else:
            return year + 1, 1, 1 #Year is incremented, month is set to January and day is set to 1

#Declaration of procedure to check validity for time travel-Helper Procedure
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

#Main function to compute days between dates
def dayBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    #To get error message if date1 > date2 is entered
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    #while loop checking if date 1 is greater than date 2

    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days = days + 1
    return days

def test():
    assert dayBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert dayBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 12, 31) == (2014, 1, 1)
    print (nextDay(2013, 10, 1))
    print (dayBetweenDates(2018, 1, 1, 2019, 1, 1))
    print ("Tests passed")


test()
print (isLeapYear(2014))
