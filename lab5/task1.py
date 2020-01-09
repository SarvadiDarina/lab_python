#
#
#
#
x=float(input('x : '))
a=float(input('a : '))
n=int(input('n : '))

s=(x + a)**2
for i in range(n - 1):
    s=(s + a)**2
print('Sum = {0}'.format(s))