import string


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fullname, age, ps, weight):
        """
        Кроме того, можно непосредственно в инициализаторе воспользоваться объектами-свойствами,
        чтобы упростить текст программы:

        def __init__(self, fullname, age, ps, weight):
            self.verify_fullname(fullname)

            self.__fullname = fullname.split()
            self.age = age
            self.passport = ps
            self.weight = weight
        Мы здесь сразу через свойства осуществляем создание приватных локальных свойств в объекте и
        автоматически проверяем корректность переданных данных. Кроме ФИО, т.к. мы для него не определяли сеттер

        Когда ты пишешь self.age = age внутри __init__, Python видит, что у тебя определен @age.setter.
        Он автоматически перенаправляет это присваивание в метод def age(self, age), где уже стоит вызов self.verify_age(age).
        Плюсы такого подхода:
        DRY (Don't Repeat Yourself): Тебе не нужно дважды вызывать verify_age (один раз в инициализаторе и один раз в сеттере).
        Ты просто один раз настраиваешь логику в сеттере, и она работает всегда — и при создании объекта, и при его изменении.
        Безопасность: Ты гарантируешь, что объект в принципе не может родиться с неправильными данными,
        потому что он проходит через те же "ворота" (сеттеры), что и при обычном редактировании.
        :param fullname:
        :param age:
        :param ps:
        :param weight:
        """
        self.verify_fullname(fullname)
        self.verify_age(age)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fullname = fullname.split()
        self.__age = age
        self.__ps = ps
        self.__weight = weight

    @classmethod
    def verify_fullname(cls, fullname):
        if not isinstance(fullname, str):
            raise TypeError('fullname must be a string')

        f = fullname.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи ФИО")

        letters = string.ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for letter in f:
            if len(letter) < 1:
                raise TypeError("В ФИО должен быть хотя бы 1 символ")
            if len(letter.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и дефис")

    @classmethod
    def verify_age(cls, age):
        if not isinstance(age, int):
            raise TypeError('age must be a integer')
        if age < 14 or age > 100:
            raise TypeError('age must be between 14 and 100')

    @classmethod
    def verify_weight(cls, weight):
        if not isinstance(weight, float):
            raise TypeError('weight must be a float')
        if weight < 20:
            raise TypeError('weight must be more than 20')

    @classmethod
    def verify_ps(cls, ps):
        if not isinstance(ps, str):
            raise TypeError('ps must be a string')
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 2 or len(s[1]) != 7:
            raise TypeError("Неверный формат паспорта")

        for letter in s[0]:
            if letter not in string.ascii_uppercase:
                raise TypeError("Серия паспорта должна состоять из 2 заглавных букв")

        if not s[1].isdigit():
            raise TypeError("Номер серии паспорта должен состоять только из цифр")

    @property
    def fullname(self):
        return self.__fullname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


p = Person("Бахтияров Шавкат Ильдарович", 18, "AD 5604207", 70.0)
print(p.__dict__)
print()
p.age = 20
print(p.__dict__)
print()
p.ps = "AS 5602209"
p.age = 200
