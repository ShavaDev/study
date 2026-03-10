"""
МАГИЧЕСКИЕ МЕТОДЫ
__getitem__(self, item) - получение значения по ключу item
__setitem__(self, key, value) - запись значения value по ключу key
__delitem__(self, key) - удаление элемента по ключу key


В объекте s1 имеется локальное свойство marks со списком студентов. Мы можем к нему обратиться и выбрать любую оценку
Но что если мы хотим делать то же самое, но используя только ссылку на объект s1,
это можно с помощью магического метода __getitem__

Теперь давайте предположим, что хотели бы иметь возможность менять оценки студентов
это можно с помощью магического метода __setitem__

Наконец, последний третий магический метод __delitem__ вызывается при удалении элемента из списка.

"""
from typing import Any


class Student:
    def __init__(self, name: str, marks: list) -> None:
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item: int) -> int:
        if 0 < item < len(self.marks):
            return self.marks[item]
        raise IndexError("Неверный индекс!")

    def __setitem__(self, key: int, value: Any) -> None: # value: int к примеру так
        """
        key это изменяемый индекс
        value это новое значение изменяемого индекса
        :param key:
        :param value:
        :return:
        """
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым не отрицательным числом!")

        # if 0 < key < len(self.marks):
        #     self.marks[key] = value
        # else:
        #     raise IndexError("Неверный индекс!")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key: int) -> None:
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым не отрицательным числом!")

        del self.marks[key]


s1: Student = Student("Shavkat", [5,5,4,3,5,4])
# print(s1.marks[2])
# print(s1[2])
# print(s1[20])
# s1[10] = 2
# print(s1.marks)
del s1[2]
print(s1.marks)