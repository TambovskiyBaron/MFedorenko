def max(x,y):
    if x > y:
        return x 
    else:
        return y 
def min(x,y):
    if x < y:
        return x
    else:
        return y    
print("Введите 4 числа")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
m1 = max(max(a,b), max(c,d))
m2 = min(min(a,b), min(c,d))
s = m1+m2
print("s =", s)