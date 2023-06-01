def bank(a,time):
    for each_year in range(time):
        a = (a * 1.1)
    return a

a=int(input("Skolko money "))
time=int(input("Na how much let "))

print(bank(a, time))