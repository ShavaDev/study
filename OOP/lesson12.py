"""
МАГИЧЕСКИЙ МЕТОД __CALL__

Магические методы также называют dunder-методы (от англ. сокращения double underscope, что значит два нижних подчеркивания)


"""



class Counter:
    def __init__(self):
        """
        Без внешних параметров def __init__(self):
        Здесь ты просто прописываешь значения внутри: self.name = "Guest".
        Как работает: Все объекты этого класса будут рождаться «клонами» с одинаковыми данными.
        Зачем: Используется, когда у объекта есть «состояние по умолчанию»
        (например, в игре у каждого нового врага по умолчанию 100 HP), которое потом изменится в процессе работы.
        """
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__counter += step
        return self.__counter



c = Counter()
c(10)



class StripChars:
    def __init__(self, chars):
        self.__chars = chars
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('args must be a string')
        return args[0].strip(self.__chars)


s1 = StripChars('?:!.; ')
s2 = StripChars(' ')
res = s1(" Hello World! ")
res2 = s2(" Hello World! ")
print(res)
print()
print(res2)

# через замыкание тоже самое
def strip_chars(chars):
    def inner(*args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('args must be a string')
        return args[0].strip(chars)
    return inner

r1 = strip_chars("?:!.; ")
print(r1(" Hello World! "))



import math

class Derivate:
    def __init__(self, func):
        self.__fn = func
        self.__counter = 0

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x+dx) - self.__fn(x)) / dx


@Derivate
def df_sin(x):
    return math.sin(x)


# df_sin = Derivate(df_sin)
print(df_sin(math.pi/4))

# через декоратор функций тоже самое
def decorator(func):
    def inner(x, dx=0.0001, *args, **kwargs):
        return (df_sin(x+dx) - df_sin(x)) / dx
    return inner

@decorator
def df_sin(x):
    return math.sin(x)


# df_sin = Derivate(df_sin)
print(df_sin(math.pi/4))



