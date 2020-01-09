#Дано два  вектори(списки) з  координатами – дійсними числами).Зясувати, чи є вектори
#перпендикулярними.
vect1 = [float(input('Координати вектора 1 : ')) for x in range(3)]
vect2 = [float(input('Координати вектора 2 : ')) for x in range(3)]
result = list(map(lambda x1, x2: x1 + x2, vect1, vect2))
if sum(result) == 0:
    print('перпендикулярні')
else:
    print('неперпендикулярні')