#  Дано два вектори (списки з координатами – дійсними числами). Знайти скалярний добуток векторів
vect1 = [float(input('Координати вектора 1: ')) for x in range(3)]
vect2 = [float(input('Координати вектора 2: ')) for x in range(3)]
scalar_dobutok = sum(list(map(lambda x, y: x * y, vect1, vect2)))
print('Скалярний добуток = {0}'.format(scalar_dobutok))
