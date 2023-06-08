
def xuloh():
    a = int(input('Число введите '))
    while a > 0:
        d = a % 10
        print(d, end=' ')
        a //= 10
xuloh()
