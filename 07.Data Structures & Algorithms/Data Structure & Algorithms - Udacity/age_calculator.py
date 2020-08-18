def daysInMonth(year, month):
    return 30


def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    """

    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False   


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""

    assert dateIsBefore(year1, month1, day1, year2, month2, day2)

    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
            

def test_nextDay():
    ### For example:
    ###    nextDay(1999, 12, 30) => (2000, 1, 1)
    print(nextDay(1999, 12, 30))

    ###    nextDay(2013, 1, 30) => (2013, 2, 1)
    print(nextDay(2013, 1, 30))

    ###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
    print(nextDay(2012, 12, 30))



def test_daysBetweenDates():
    test_cases = [((2012,9,30,2012,10,30),30), 
            ((2012,1,1,2013,1,1),360),
            ((2012,9,1,2012,9,4),3),
            ((2013,1,1,1999,12,31), "AssertionError")]

    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result == answer and answer != "AssertionError":
                print("Test case passed!")
            else:
                 "Test with data:", args, "failed"

        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))  

if __name__ == "__main__":
    #test_nextDay()
    #test_daysBetweenDates()

    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1

