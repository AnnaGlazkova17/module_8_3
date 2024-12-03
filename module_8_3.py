class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            True
        else:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number >= 1000000 and vin_number <= 9999999:
            True
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            True
        else:
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        if len(numbers) == 6:
            True
        else:
            raise IncorrectCarNumbers('Неверная длина номера')
    def __init__(self, model, __vin, __numbers):
        self.model = model
        if self._Car__is_valid_vin(__vin):
            self.__vin = __vin
        if self._Car__is_valid_numbers(__numbers):
            self.__number = __numbers


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

