#Використовуючи підпрограми для додавання векторів та
# множення вектора на число, знайти вектор
#c=a-3*b+2*c, де a,b,c .
def enter_vector(name):
	return [int(input('Введіть {0} координату вектора {1}: '.format(x,name))) for x in range(3)]

def multiply_vector(vector, scalar):
	return list(map(lambda coordinate: coordinate * scalar, vector))

def add_vector(v1, v2):
	return list(map(lambda x,y: x + y, v1, v2))

a = enter_vector('a')
b = enter_vector('b')
c = enter_vector('c')

_3b = multiply_vector(b, -3)
c2 = multiply_vector(c, 2)
s1 = add_vector(a, _3b)
res = add_vector(s1, c2)
print(res)


