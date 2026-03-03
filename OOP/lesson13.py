"""
МАГИЧЕСКИЕ МЕТОДЫ __str__, __repr__, __len__, __abs__

__str__() – магический метод для отображения информации об объекте класса для пользователей
(например, для функций print, str);
__repr__() – магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков).

__len__() – позволяет применять функцию len() к экземплярам класса;
__abs__() - позволяет применять функцию abs() к экземплярам класса.
"""

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        """
        служит для вывода какой-то отладочной информации
        :return:
        """
        return f"{self.__class__}: {self.name}"

    def __str__(self):
        """
        служит для вывода информации для пользователя
        :return:
        """
        return f"{self.name}"


class Point:
    def __init__(self, *args):
        self.__coordinates = args

    def __len__(self):
        return len(self.__coordinates)

    def __abs__(self):
        return list(map(abs, self.__coordinates))

point = Point(-1, 2)
print(len(point))
print(abs(point))