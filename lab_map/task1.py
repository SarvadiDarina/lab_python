#Дано два вектори (списки з координатами – дійсними числами).
# Знайти суму векторів.
vect1 = [float(input('Координати вектора1: ')) for x in range(3)]
vect2 = [float(input('Координати вектора2: ')) for x in range(3)]
suma= map(lambda x, y : x + y, vect1, vect2)
print(list(suma))
