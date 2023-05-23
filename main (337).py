def derevo():
    k=0
    ans = input("Отгадайте загадку, у вас 5 попыток - Зимой и летом одним цветом:")
    if ans == "Елка" or "елка":
       print("Правильно")
       break
    else:
       k += 1
       if (k >= 5):
          print("Лох")
          break
       print("Неправильно, это была ваша", k, "попытка")
       continue
derevo()
