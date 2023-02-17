a = 1
b = 2
print((a>b) and (b>a))
print((b>a) and (a<b))
print((a>b) or (b>a))
print(not (b>a))
c = a + b
print((c>b) or (b>a))
print((a>c) or (b>c))
print((c<b) or (b<a))
print((a<c) or (b>a))
d = 'Бешбармак'
e = 'Марилов Никита Михайлович'
print((e>d) and (d>e))
print ((d>e) or (d>e))
print((e>d) or (e<d))
print(not(d<e))