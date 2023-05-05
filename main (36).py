from random import randint
n = randint(1,100)
i=1
print("Отгадайте число за 100 попыток")
while i <= 100:
    u = int(input(str(i) + "-я попытка: "))
    if u > n:
        print("Больше чем загадано")
    elif u < n:
        print("Меньше чем загадано")
    else:
        print("Угадано с %d-й попытки" % i)
        break
    i += 1
else:
    print("Попытки кончились,  Было загадано", n)