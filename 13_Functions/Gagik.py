def date(day, month, year):
 if(year == 0):
        return False
 else:
    if(year % 4 == 0 and year % 10 != 0 or year % 10 ==0 and year % 400 == 0):
        if month < 1 or month > 12:
            return False
        else:
            if (day < 1 or day > 31):
                return False
            else:
                months_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                if (day >= 1 and day <= months_days[month - 1]):
                    return True
                else:
                    return False
    else:
        if month < 1 or month > 12:
            return False
        else:
            if(day < 1 or day > 31):
                return False
            else:
                months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                if (day >= 1 and day <= months_days[month - 1]):
                    return True
                else:
                    return False

day = int(input('The day - '))
month = int(input("The month - "))
year = int(input("The year - "))
conclusion = date(day, month, year)
print(conclusion)