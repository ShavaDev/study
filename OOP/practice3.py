"""Задача: «Умная Система Учета Лабораторных Экспериментов»"""

from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime


# кастомные исключения
class ChemicalReactionError(Exception):
    """Выбрасывается, когда пытаемся смешать разные вещества."""
    pass


@dataclass
class Substance:
    name: str  # название вещества
    density: float  # плотность
    boiling_point: float = 0  # температура кипения

    def __post_init__(self) -> None:
        self.name = self.name
        self.density = self.density

    @property
    def density(self) -> float:
        return self._density

    @density.setter
    def density(self, value: float | int) -> None:
        if value < 0 or not isinstance(value, (float, int)):
            raise ValueError("density must be a positive number")

        self._density = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or not value:
            raise ValueError("name must be a string and must be a non-empty string")

        self._name = value


class TemperatureControlled:
    def __set__(self, instance: Container, value: int | float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError("temperature must be a number")

        boiling_limit = instance._substance.boiling_point

        if value > boiling_limit:
            # Логика испарения
            print(f"[{datetime.now().strftime('%H:%M:%S')}] [BOOM] "
                  f"{instance._substance.name} reached {value}°C and evaporated!")
            instance._volume = 0
            instance._current_temp = value
        else:
            print(f"Temperature set to {value}°C")
            instance._current_temp = value

    def __get__(self, instance, owner):
        return getattr(instance, '_current_temp', 20.0)


class Container:
    MAX_VOLUME: int = 1000  # см^3
    temperature = TemperatureControlled()

    def __init__(self, volume: float | int, substance: Substance, material: str) -> None:
        if not isinstance(volume, (float, int)):
            raise ValueError("volume must be a number")

        if volume < 0 or volume > self.MAX_VOLUME:
            raise ValueError("Volume must be between 0 and {}".format(self.MAX_VOLUME))

        self._substance = substance
        self._volume = volume
        self.meta = self.Meta(owner=self, material=material, last_serviced=datetime.now())

    @property
    def current_weight(self):
        return self._substance.density * self._volume

    def __add__(self, other: Container) -> Container:
        if not isinstance(other, Container):
            raise TypeError("You can only add containers to containers")

        if other._substance != self._substance:
            raise ChemicalReactionError("Substance names do not match")

        new_volume = self._volume + other._volume
        if new_volume > self.MAX_VOLUME:
            raise ValueError("Volume cannot be greater than {}".format(self.MAX_VOLUME))

        return Container(volume=new_volume, substance=self._substance)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._substance.name}, vol: {self._volume}, weight: {self.current_weight})"

    class Meta:
        def __init__(self, owner: Container, material: str, last_serviced: datetime):
            self._owner = owner
            self._material = material
            self._last_serviced = last_serviced

        def get_info(self):
            return f"Контейнер из {self._material}, внутри {self._owner._substance.name}"



# TESTS
# 1. Создаем серную кислоту
acid = Substance(name="Sulfuric Acid", density=1.84, boiling_point=337)
c1 = Container(volume=100, substance=acid, material="Special Glass")

# 2. Проверяем вес и информацию из меты
print(f"Weight: {c1.current_weight}g")
print(c1.meta.get_info())

# 3. Нагреваем!
c1.temperature = 100  # Нормально
c1.temperature = 400  # [BOOM] Испарение!

# 4. Проверяем объем после испарения
print(f"Volume after heat: {c1._volume}")