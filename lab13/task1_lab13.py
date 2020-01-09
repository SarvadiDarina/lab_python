from math import sqrt

class Triangle:
    def __init__(self, a, b, c):
        if a < 0 or b < 0 or c < 0:
            raise Exception('Сторона не може бути відємною')
        self.a = a
        self.b = b
        self.c = c

    def set_side(self):
        self.a = int(input('a = '))
        self.b = int(input('b = '))
        self.c = int(input('c = '))
        return self.a, self.b, self.c

    def get_side(self):
        return self.a, self.b, self.c

    def get_square(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def get_perimeter(self):
        return (self.a + self.b + self.c)

    def __add__(self, other):
        return Triangle(self.a + other, self.b + other, self.c + other)

    def __sub__(self, other):
        return Triangle(self.a - other, self.b - other, self.c - other)

    def __mul__(self, other):
        return Triangle(self.a * other, self.b * other, self.c * other)

    def __str__(self):
        return "Нові сторони - {0}, {1}, {2}".format(self.a, self.b, self.c)

class TrianglePrizma(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        if h < 0:
            raise Exception('Неправильна сторона')
        self.h = h

    def get_volume(self):
        return super().get_square() * self.h

    def get_square(self):
        bases = 2 * super().get_square()
        side1 = self.a * self.h
        side2 = self.b * self.h
        side3 = self.c * self.h
        return bases + side1 + side2 + side3

    def __add__(self, other):
        return TrianglePrizma(self.a + other, self.b + other, self.c + other, self.h + other)

    def __sub__(self, other):
        return TrianglePrizma(self.a - other, self.b - other, self.c - other, self.h - other)

    def __mul__(self, other):
        return TrianglePrizma(self.a * other, self.b * other, self.c * other, self.h * other)

    def __str__(self):
       return 'Сторони трикутної призми - {0}, {1}, {2} і {3}'.format(self.a, self.b, self.c, self.h)

prizma = TrianglePrizma(3,4,5,10)
print('Сторони призми - {0}'.format(prizma.get_side()))
print('Площа поверхні - {0}'.format(prizma.get_square()))
print('Обєм призми становить {0}'.format(prizma.get_volume()))
print('Додано {0}, Нові сторони - {1}'.format(7, prizma + 7))
print('{0}: {1}'.format(100, prizma * 100))
print(prizma.set_side())
print(prizma.get_side())