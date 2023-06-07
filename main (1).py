day = int(input("Введите день: \n"))
month = int(input("Введите номер месяца: \n"))
year = int(input("Введите год: \n"))
def date(day, month, year):
    if day >= 0 or month >= 0 or year >= 0:
        return False
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month <= 12:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return True
print(date(day, month, year))
date(day, month, year)