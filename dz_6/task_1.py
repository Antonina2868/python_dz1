# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def calc(first, step, n):
    return first + (n-1)*step

a1 = int(input("Введите первое число: "))
d_step = int(input("Введите шаг арифметической прогрессии: "))
el_num = int(input("Введите количество цифр: "))
# i = 1
# arr = []
# while (i <= el_num):
#     arr.append(calc(a1,d_step,i))
#     i += 1
# print(arr)

arr = []
for i in range(el_num):
    arr.append(calc(a1, d_step, i+1))
print(arr)



