# Нехай x0=x1, xi=xi-1 +  2xi-2 , де i=2,3,....
# Визначити xn .
i = int(input('Введіть i = '))

def rec(i):
    if i == 0 or i == 1:
        return 1
    else:
        return rec(i-1) + 2*rec(i-2)

print('i({0}) = {1}'.format(i, rec(i)))

