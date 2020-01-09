#Дано типізований файл, який містить квадратну матрицю A(nxn)
# (матриця зберігається поелементно, кількість елементів визначити
# за допомогою функції FileSize). Визначити найменший елемент серед
# додатних використовуючи динамічно створений двовимірний масив.
# Від’ємні елементи зберегти у окремому файлі дійсних чисел «V.dat».
with open('2.txt') as file:
    numbers = []
    file_list = file.read().splitlines()
    num_list = [int(j) for i in file_list for j in i.split()]
    count_el = len(num_list)
    print('Розмір матриці становить {0}x{1}'.format((count_el//2), (count_el//2)))

with open('vid.txt', 'w') as file:
    negative_nums = [el for el in num_list if el < 0]
    for i in range(len(negative_nums)):
        file.write(str(negative_nums[i]))
