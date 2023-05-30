def is_year_leap(year):
    if year % 100 == 0:
        if year %  400 == 0:
            return "Год високосный"
        else:
            return "Год не високосный"

    elif year % 4 == 0:
        return "Год високосный"

    else:
        return "Год не високосный"

x = is_year_leap(int(input('Введите год: ')))
print(x)