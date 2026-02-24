"""Документация по декораторам

декоратор – это функция, которая принимает ссылку
на другую функцию и расширяет ее функциональность за счет вложенной функции.

Часто, чтобы не создавать новые имена функций, вместо имени f используют то же самое имя функции

Однако, если сейчас в нашу функцию some_func() добавить хотя бы один параметр
А, затем, вызвать ее с одним аргументом
то увидим ошибку, так как внутренняя функция wrapper() прописана без параметров.
А именно на нее и ссылается сейчас some_func. В самом простом варианте, мы, конечно,
может просто добавить этот параметр для wrapper()
И теперь программа будет запускаться без ошибок.
Но, очевидно, она перестанет работать, если число параметров функции func() изменится.
Как описать универсальную реализацию декоратора для функций с разным числом фактических и формальных параметров?
Конечно, для этого нужно определить вложенную функцию, принимающую произвольное число аргументов, следующим образом
*args, **kwargs
А, затем, переданные значения распаковываются и передаются функции func(). Получаем универсальную реализацию декоратора.

И, наконец, последний штрих. Сама по себе функция some_func() может возвращать какие-либо значения, например,
помимо вывода сообщения в консоль, она еще будет возвращать сформированную строку:

def some_func(title, tag):
    print(f"title = {title}, tag = {tag}")
    return f"<{tag}>{title}</{tag}>"
Но, при попытке получить сейчас это значение:

some_func = func_decorator(some_func)
res = some_func("Python навсегда!", 'h1')
print(res)
Увидим None. И я, думаю, вы прекрасно понимаете почему? Да, это потому, что вложенная функция wrapper()
ничего не возвращает. Исправим это и сделаем так, чтобы она возвращала значение функции func():

def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("------ что-то делаем перед вызовом функции ------")
        res = func(*args, **kwargs)
        print("------ что-то делаем после вызова функции ------")
        return res

    return wrapper
Вот теперь получили окончательную версию универсального декоратора функции
и при выполнении программу видим не только его работу, но и возвращенное функцией значение.

Декораторы можно навешивать (применять) к функциям с помощью специального значка @. То есть, вместо строчек:

get_nod = timer(get_nod)
get_fast_nod = timer(get_fast_nod)
достаточно перед объявлением функций прописать @timer. В результате, эти функции, как бы,
«обертываются» нашим декоратором timer и расширяются его функционалом. Если мы теперь запустим программу,
то увидим тот же самый результат. А вот если у какой-либо функции уберем эту строчку,
то будет обычный вызов без оценки скорости работы. Фактически, запись:

@timer
def get_nod(a, b):
    ...
эквивалентна строчке:

get_nod = timer(get_nod)



def decorator(func):  # Сюда передаём функцию которую нужно декорировать
    def wrapper(*args, **kwargs):  # Сюда передаём аргументы декорированной функции
        print(f'{func.__name__} started')  # декорирующие действия 1
        result = func(*args, **kwargs)  # *args -чтобы работать с разным кол-вом аргументов
        print(f'{func.__name__} finished')  # декорирующие действия 2
        return result  # возвращаем результат

    return wrapper  # передаём ссылку на вложенную функцию


@decorator  # сахар для вызова декоратора (навешиваем декоратор)
def summ(a, b):  # функция которую нужно декорировать в этот момент: summ = wrapper
    return a + b


print(summ(2, 3))


def repeat(times):
    # Внешняя функция, принимающая параметр декоратора
    def decorator(func):
        # Внутренняя функция, принимающая целевую функцию
        def wrapper(*args, **kwargs):
            # Логика декоратора
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Применение декоратора с параметром
@repeat(times=3)
def greet(name):
    print(f"Привет, {name}!")

greet("Анна")



from functools import ...


functools.cache: Простой легковесный кэш для функций.
functools.cached_property: Преобразует метод класса в свойство, значение которого вычисляется один раз и затем кэшируется.
functools.cmp_to_key: Преобразует функцию сравнения в key-функцию.
functools.lru_cache: Декоратор для кэширования результатов функции с ограничением по размеру кэша.
functools.partial: Позволяет зафиксировать некоторые аргументы функции и создать новую функцию с меньшим количеством аргументов.
functools.partialmethod: Похож на partial, но используется для методов классов.
functools.reduce: Применяет функцию к элементам последовательности, сводя её к одному значению.
functools.singledispatch: Декоратор для создания одноаргументных обобщённых функций.
functools.singledispatchmethod: Похож на singledispatch, но используется для методов классов.
functools.total_ordering: Декоратор класса, который автоматически добавляет методы сравнения.
functools.update_wrapper: Обновляет атрибуты обёртки функции, чтобы они соответствовали оригинальной функции.
functools.wraps: Декоратор для сохранения метаданных оригинальной функции при создании декораторов.
Эти функции помогают оптимизировать код, улучшить его читаемость и повторное использование.


"""

# import time
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         dif = end - start
#         print(f"Время работы функции {func.__name__} {dif} секунд")
#         return result
#
#     return wrapper
#
#
# @timer
# def get_slow_nod(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#
#     return a
#
#
# @timer
# def get_fast_nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b:
#         a, b = b, a % b
#
#     return a
#
#
# # get_slow_nod = timer(get_slow_nod)
# # get_fast_nod = timer(get_fast_nod)
#
# result1 = get_slow_nod(80, 1_000_000_000)
# result2 = get_fast_nod(80, 1_000_000_000)
# print(result1, result2)


## декораторы функций с параметрами

# import math
#
#
# def df_decorator(dx=0.01):
#     def func_decorator(func):
#         def wrapper(x, *args, **kwargs):
#             return (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#
#         wrapper.__name__ = func.__name__
#         wrapper.__doc__ = func.__doc__
#         return wrapper
#
#     return func_decorator
#
#
# @df_decorator(dx=0.0001)
# def df_function(x):
#     return math.sin(x)
#
#
# # f = df_decorator(dx=0.0001) # эти две строчки то же самое @df_decorator
# # df_function = f(df_function)
#
# df = df_function(math.pi / 3)
# print(df)


# def decorator(func):
#     def wrapper(s1, s2):
#         s1, s2 = func(s1, s2)
#         d = {}
#         lst1 = s1.split()
#         lst2 = s2.split()
#         i = 0
#         j = 0
#         while len(d) != len(lst1):
#             d[lst1[i]] = lst2[j]
#             i += 1
#             j += 1
#         return sorted(d.items())
#
#     return wrapper
#
#
# def lists(s1, s2):
#     return s1, s2
#
#
# f = decorator(lists)
#
# print(*f("house river tree car", "дом река дерево машина"))


# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
#
# def slug(func):
#     def wrapper(s, *args, **kwargs):
#         res = func(s, *args, **kwargs)
#         while "--" in res:
#             res = res.replace("--", "-")
#         return res
#
#     return wrapper
#
#
# @slug
# def stroka(s):
#     s = s.lower()
#     res = ""
#     for ch in s:
#         if ch in t:
#             res = res + t[ch]
#         elif ch in " :;,._":
#             res += "-"
#         else:
#             res += ch
#     return res
#
#
# r = stroka(input())
# print(r)


# from functools import wraps
#
#
# def limit_calls(max_calls: int):
#     def decorator(func):
#         count = 0
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             if count >= max_calls:
#                 print("Лимит вызова функции исчерпан!")
#                 return
#             func(*args, **kwargs)
#             count += 1
#
#         return wrapper
#
#     return decorator
#
#
# @limit_calls(max_calls=5)
# def spam():
#     print("spam")
#
#
# spam()
# spam()
# spam()
# spam()
# spam()
# spam()
