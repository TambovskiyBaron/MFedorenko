def derevo():
    k=0
    while k < 5:
        ans = input("Отгадайте загадку, у вас 5 попыток - Зимой и летом одним цветом:")
        if ans == "Елка":
            print("Правильно")
            break
        else:
            k += 1
            print("НеправильноБ это была ваша", k, "попытка")
            if (k >= 5):
                print("Лох")
derevo()
