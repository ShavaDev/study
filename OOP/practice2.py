"""
Проект «Строгий Тимлид»
"""

class ValidatorMeta(type):
    def __new__(cls, name, bases, attrs):
        # 1. Проверка документации
        # Мы смотрим именно в attrs, так как сам объект класса еще не создан
        if not attrs.get("__doc__") or attrs["__doc__"].strip() == "":
            raise TypeError(f"В классе <{name}> отсутствует документация!")

        # 2. Проверка имен методов
        for key, value in attrs.items():
            # Пропускаем магические методы (__init__, __str__ и т.д.)
            if key.startswith("__") and key.endswith("__"):
                continue

            # Проверяем только то, что является функцией (методом)
            if callable(value):
                if "_" in key:
                    raise TypeError(
                        f"Метод <{key}> в классе <{name}> нарушает стиль! "
                        f"Используйте camelCase (например: {key.replace('_', '')})"
                    )

        return type.__new__(cls, name, bases, attrs)


class Test(metaclass=ValidatorMeta):
    """__doc__"""

    def __init__(self):
        print("init called")

    def case_camel(self):
        print("case_camel called")

    def __private(self):
        print("__private called")

    def test__(self):
        pass

t = Test()