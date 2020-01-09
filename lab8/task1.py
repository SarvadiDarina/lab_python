#За даними дійсними числами a і b  обчислити u
from math import sin, cos

def suma(x):
    if x > 3:
        m = 0
        for i in range(1, 7):
            m += sin(x**i)
        return m
    else:
        z = -1
        m = 0
        a = cos(x)
        for i in range(1, 6):
            m = m + z*a
            a = cos(a)
            z = -z
        return m


a = int(input('Введіть a = '))
b = int(input('Введіть b = '))
if suma(a) > suma(b):
    print(suma(b))
else:
    print(suma(a))

