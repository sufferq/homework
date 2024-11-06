class Car:
    def __init__(self, model: str, __vin: int, __numbers: str):
        self.model = model
        self.vin = __vin
        self.numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, vin_numbers):
        if not isinstance(vin_numbers, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_numbers < 1000000 or vin_numbers > 9999999:
            raise IncorrectVinNumber('Неверный диапозон для vin')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

if __name__ == '__main__':

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