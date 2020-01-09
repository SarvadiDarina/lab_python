import math
#The triangle is given by its coordinates
x1=int(input('Enter x1 '))
y1=int(input('Enter y1 '))
x2=int(input('Enter x2 '))
y2=int(input('Enter y2 '))
x3=int(input('Enter x3 '))
y3=int(input('Enter y3 '))
#determine if this triangle is obtuse
a=math.sqrt(((x2-x1)**2)+(y2-y1)**2)
b=math.sqrt(((x3-x2)**2)+(y3-y2)**2)
c=math.sqrt(((x3-x1)**2)+(y3-y1)**2)

cosa=(b**2 + c**2 - a**2)/(2*b*c)
cosb=(b**2 + a**2 - c**2)/(2*b*a)
cosc=(a**2 + c**2 - b**2)/(2*a*c)
if cosa<0 or cosb<0 or cosc<0:
    print('Тупокутний')
else:
    print('Не тупокутний')

