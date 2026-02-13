"""Документация по замыканиям

Замыкание — это функция, которая:

объявлена внутри другой функции

использует переменные внешней функции

продолжает иметь доступ к этим переменным после завершения внешней функции

Иными словами:

Замыкание = функция + сохранённое окружение

Области видимости (LEGB)

Python ищет имена переменных в следующем порядке:

Local — локальная область текущей функции

Enclosing — область внешней функции (замыкание)

Global — область модуля

Builtins — встроенные имена

Переменные замыкания относятся к уровню Enclosing.

Как работает замыкание внутри Python

При создании вложенной функции Python анализирует:

какие имена используются, но не являются локальными

Для таких имён создаются closure-cells

Эти ячейки:

хранят ссылки на значения

живут в куче (heap)

Пока жива функция, жива и её __closure__

Важно:

замыкание хранит только реально используемые переменные

не всё окружение, а минимально необходимое

Ключевое различие: чтение и изменение

Для чтения enclosing-переменных nonlocal не нужен

Для изменения enclosing-переменной nonlocal обязателен

Жизненный цикл замыкания

Внешняя функция завершается

Её локальные переменные уничтожаются

НО переменные, захваченные замыканием, остаются

Они уничтожаются только когда исчезает последняя ссылка на функцию

Что замыкание НЕ делает

не хранит аргументы вызовов автоматически

не сохраняет локальные переменные каждого вызова

не является глобальным состоянием

Замыкание и состояние

Замыкания позволяют:

хранить состояние без глобальных переменных

создавать функции с “памятью”

реализовывать декораторы, счётчики, кэши

Когда использовать замыкания

при создании декораторов

при параметризации поведения функций

когда нужен инкапсулированный state без классов
"""

# def main_func(name):
#     def inner_func():
#         print("hello friend", name)
#
#     return inner_func
#
#
# i = main_func("Ivan")
# print(i)
# v = main_func("Victor")
# v()


# def adder(value: int):
#     def inner(a: int):
#         return a + value
#
#     return inner
#
#
# a2 = adder(2)
# print(a2(3))


# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#
#     return inner


# def average_nums():
#     nums = []
#
#     def inner(num):
#         nums.append(num)
#         return sum(nums) / len(nums)
#
#     return inner
#
# n1 = average_nums()
#
# n1(5)
# n1(10)
# print(n1(5))
# print(n1(10))

# from datetime import datetime
# import time
#
#
# def timer():
#     start = datetime.now()
#
#     def inner():
#         return datetime.now() - start
#
#     return inner
#
#
# r1 = timer()
# time.sleep(2)
# print(r1())
# time.sleep(1)
# print(r1())


# def add(a, b):
#     return a + b
#
#
# def counter(func):
#     count = 0
#
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f"Функция {func.__name__} вызывалась {count} раз")
#         return func(*args, **kwargs)
#
#     return inner
#
#
# c = counter(add)
# print(c(10, 20))
