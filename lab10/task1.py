#	Об’єкт “Число”
class Number:
    def __init__(self, number):
        self.number = number

    def enter_num(self):
        #self.number = int(input('Введіть число: '))
        return self.number

    def print_num(self):
        print(self.number)

    def num_count(self):
        return len(str(self.number))

    def sum_nums(self):
        return sum(map(int, str(self.number)))

    def __str__(self):
        return str(self.number)


num = Number( 1265)
print('Число {0}'.format(num.print_num()))
print('Кількість цифр у числі {0} -  {1}'.format(num, num.num_count()))
print('Сума цифр у числі {0} - {1}'.format(num, num.sum_nums()))
num.enter_num()
num.print_num()