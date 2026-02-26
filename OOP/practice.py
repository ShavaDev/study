"""
Проект: "SmartProfile Engine"
"""

import string


class StringValidator:
    """
    считаю что строка у меня должна состоять только из букв и пробелов, без цифр
    """
    MIN_SIZE = 6
    MAX_SIZE = 18
    LETTERS = (
            string.ascii_letters +
            "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" +
            "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()
    )

    @classmethod
    def string_validate(cls, st):
        if not isinstance(st, str):
            raise ValueError("String must be a string")

        # Твоя проверка на наличие букв
        if not any(char in cls.LETTERS for char in st):
            raise ValueError("Строка должна содержать буквы")

    def __set_name__(self, owner, name):
        print(f"!!! связываю дескриптор с именем {name} в классе {owner.__name__}")
        self.name = "_" + name
        print(self.__dict__)

    def __get__(self, instance, owner):
        print(f"считываю атрибут {self.name} класса {owner.__name__}")
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        print(f"вставляю новые данные '{value}' атрибута {self.name}")
        self.string_validate(value)
        setattr(instance, self.name, value)


class EmailValidator:
    MUST_AT = "@"
    MUST_POINT = "."

    @classmethod
    def email_validate(cls, email):
        if not isinstance(email, str):
            raise ValueError("Email must be a string")

        at = email.find(cls.MUST_AT)
        point = email.find(cls.MUST_POINT)
        if at == -1 and point == -1:
            raise ValueError("Email must contain '@' and '.'")

        # if at != point - 1:
        #     raise TypeError("'@' must go right before '.' ")

    def __set_name__(self, owner, name):
        print(f"!!! связываю дескриптор с именем {name} в классе {owner.__name__}")
        self.name = "_" + name
        print(self.__dict__)

    def __get__(self, instance, owner):
        print(f"считываю атрибут {self.name} класса {owner.__name__}")
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        print(f"вставляю новые данные '{value}' атрибута {self.name}")
        self.email_validate(value)
        setattr(instance, self.name, value)


class DateValidator:
    MIN = 1950
    MAX = 2026

    @classmethod
    def date_validate(cls, date):
        if not isinstance(date, int):
            raise ValueError("Date must be a integer")
        if date < cls.MIN or date > cls.MAX:
            raise ValueError("Date must be between '1950' and '2026'")

    def __set_name__(self, owner, name):
        print(f"!!! связываю дескриптор с именем {name} в классе {owner.__name__}")
        self.name = "_" + name
        print(self.__dict__)

    def __get__(self, instance, owner):
        print(f"считываю атрибут {self.name} класса {owner.__name__}")
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        print(f"вставляю новые данные '{value}' атрибута {self.name}")
        self.date_validate(value)
        setattr(instance, self.name, value)


class Person:
    fullname = StringValidator()

    age = DateValidator()
    email = EmailValidator()

    def __init__(self, fullname, age, email):
        self.fullname = fullname
        self.age = age
        self.email = email


# testing
p1 = Person("Бахтияров Шавкат Ильдарович", 2000, "shava_dev@mail.com")
p2 = Person("       ", 2022, "some@mail.com")
p3 = Person("Some Thing", 2027, "some2@mail.com")
p4 = Person("Some Thing 2", 1980, "some mail com")