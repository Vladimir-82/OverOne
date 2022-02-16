from random import randint
from time import time


# ex0
# def turp(object):
#     """
#     Считате колличество слов в эелементах кортежа
#     :param object:
#     :return:
#     """
#     for arg in object:
#         print(f'Слово - {arg}, его длина - {len(arg)}')
#
#
# def lst(object):
#     """
#     Считате колличество букв и цифр в списке
#     :param object:
#     :return:
#     """
#     counter_letters = 0
#     counter_numbers = 0
#     for arg in object:
#         if isinstance(arg, int):
#             counter_numbers += 1
#         if isinstance(arg, str):
#             counter_letters += 1
#     print(f'Букв в списке - {counter_letters}, цифр в списке - {counter_numbers}')


# def number(object):
#     '''
#     Считает колличество нечетных цифр
#     :param object:
#     :return:
#     '''
#     counter_odd = 0
#     for el in str(object):
#         if int(el) % 2:
#             counter_odd += 1
#     print(f'Колличество нечетных цифр - {counter_odd}')
#
#
# def string(object):
#     """
#     Считает колличество букв в строке
#     :param object:
#     :return:
#     """
#     counter_letters = 0
#     for i in object:
#         if i.isalpha():
#             counter_letters += 1
#
#     print(f'Колличество букв - {counter_letters}')


# obj = 'rt48'
#
# if isinstance(obj, tuple):
#     turp(obj)
# elif isinstance(obj, list):
#     lst(obj)
# elif isinstance(obj, int):
#     number(obj)
# elif isinstance(obj, str):
#     string(obj)
# else:
#     print('Unknown type')




# ex1

# def func1():
#     """
#     рандомные числа
#     :return:
#     """
#     res = [randint(1, 10) for _ in range(10)]
#     print(res)
#     return res
#
# def count(lst):
#     """
#     считаем колличество элементов в списке
#     :param lst:
#     :return:
#     """
#     [print(f'Колличество элементов {i} - {lst.count(i)}') for i in lst]
# res = func1()
# count(res)




# ex2

# def func(args):
#     """
#     минимум и максисум списка
#     :param args:
#     :return:
#     """
#     return f'Минимум в списке - {min(args)} Максимум в списке - {max(args)}'
#
# print(func([4,6,1,9]))




# ex3
# def season(n):
#     """
#     Месяц по числу
#     :param n:
#     :return:
#     """
#     year = dict(zip([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#                     ['January', 'February',
#                     'March', 'April', ' May',
#                     'June', 'July', 'August',
#                     'September', 'October', 'November',
#                     'December'])
#                 )
#     return year[n]

# print(season(12))




# ex4
# def func(a, b, c):
#     '''
#     Вычисляем корни квадратного уравнения
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     '''
#     D = b ** 2 - 4 * a * c
#     if D > 0:
#         return (-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)
#     elif D == 0:
#         return - b / (2 * a)
#     else:
#         return 'Корней нет'
#
# print(func(4, -7, -2))




# ex5
# def func(n):
#     """
#     Функция вычисления факториала
#     :param n:
#     :return:
#     """
#     if n != 0:
#         return n * func(n - 1)
#     else:
#         return 1
#
# print(func(3))



# ex6
# def func(lst1, lst2):
#     """
#     Опрделяем общие элементы списков
#     :param lst1:
#     :param lst2:
#     :return:
#     """
#     return set(lst1).intersection(lst2)
#
#
# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6, 7]
# res = func(l1, l2)
# print(*res)



# ex7
# def three_args(var1=None, var2=None, var3=None):
#     '''
#     Печатает аргументы, которые не равны None
#     :param var1:
#     :param var2:
#     :param var3:
#     :return:
#     '''
#     args = (var1, var2, var3)
#     [print(var) for var in args if var != None]
#
# three_args(var1=1, var2=2)




# ex8
# def func(a, b):
#     """
#     Суммирует чила от a до b
#     :param a:
#     :param b:
#     :return:
#     """
#     if a > b:
#         a, b = b, a
#     return sum(list(range(a, b + 1)))
#
# print(func(3, 1))



# ex9
# def triangle(a, b, c):
#     """
#     Определяет существует ли триугольник
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     """
#     return 'exist' if (a + b > c) and (a + c > b) and (b + c > a) else 'not exist'
#
# print(triangle(100, 125, 50))





# ex10 + decorator

# def add_info(some_func):
#     def surogate(some_args):
#         print('Какой-то текст до функции')
#         res = some_func(some_args)
#         return res
#     return surogate
#
#
#
# @ add_info
# def func(lst):
#     return [el for el in lst if type(el) == int or type(el) == float]
#
# params = [16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']
# print(sorted(func(params)))



# ex 11 decorator time track

# def time_track(func):
#     def surogate(*args):
#         start = time()
#         f = func(*args)
#         finish = time()
#         res = finish - start
#         print(f'Функция считает - {round(res, 2)} сек')
#         return f
#     return surogate
#
# @time_track
# def counter(*args):
#     result = 1
#     for arg in args:
#         result *= arg ** 5000
#     return result
#
# print(counter(10000, 30000, 50000))