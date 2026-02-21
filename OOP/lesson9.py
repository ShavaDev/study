"""
PROPERTY

"""

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self): # get_age
        return self.__age

    @age.setter
    def age(self, age): # set_age
        self.__age = age

    @age.deleter
    def age(self): # del_age
        del self.__age

    # age = property()
    # age = age.setter(set_age)
    # age = age.getter(get_age)
    # age = age.deleter(del_age)

p = Person("John", 20)
a = p.age
p.age = 35
del p.age
p.age = 15
print(p.__dict__)