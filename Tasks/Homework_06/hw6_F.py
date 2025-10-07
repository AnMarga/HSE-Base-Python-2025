import sys

class StringValue:
    def __init__(self, min_length: int, max_length: int):
        self.min_length = min_length
        self.max_length = max_length
        self._name = None

    def __set_name__(self, owner, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if isinstance(value, str) and self.min_length <= len(value) <= self.max_length:
            setattr(instance, self._name, value)


class PriceValue:
    def __init__(self, max_value: float):
        self.max_value = max_value
        self._name = None

    def __set_name__(self, owner, name):
        self._name = '_' + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if isinstance(value, (int, float)) and 0 <= value <= self.max_value:
            setattr(instance, self._name, value)


class Car:
    name = StringValue(2, 50)
    price = PriceValue(2_000_000)

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class AutoSalon:
    def __init__(self, name: str):
        self.name = name
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)


exec(sys.stdin.read())
