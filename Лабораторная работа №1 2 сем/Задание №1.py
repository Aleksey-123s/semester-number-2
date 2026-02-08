import doctest


class Clock:
    """
    Класс, представляющий часы.

    Attributes:
        brand (str): Бренд часов
        type (str): Тип часов (механические, электронные, кварцевые)
        hour (int): Текущий час (0-23)
        minute (int): Текущая минута (0-59)
    """

    def __init__(self, brand: str, type: str, hour: int = 0, minute: int = 0):
        """
        Создание и подготовка к работе объекта "Часы"

        :param brand: Бренд часов
        :param type: Тип часов
        :param hour: Начальный час (0-23)
        :param minute: Начальная минута (0-59)

        :raise TypeError: Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если время установлено некорректно

        Примеры:
        >>> clock = Clock("Casio", "электронные", 10, 30)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not isinstance(type, str):
            raise TypeError("Тип часов должен быть строкой")
        if not isinstance(hour, int):
            raise TypeError("Час должен быть целым числом")
        if not isinstance(minute, int):
            raise TypeError("Минута должна быть целым числом")
        if hour < 0 or hour > 23:
            raise ValueError("Час должен быть в диапазоне от 0 до 23")
        if minute < 0 or minute > 59:
            raise ValueError("Минута должна быть в диапазоне от 0 до 59")

        self.brand = brand
        self.type = type
        self.hour = hour
        self.minute = minute

    def set_time(self, hour: int, minute: int) -> None:
        """
        Установка времени на часах.

        :param hour: Час для установки (0-23)
        :param minute: Минута для установки (0-59)
        :raise TypeError: Если аргументы не являются целыми числами
        :raise ValueError: Если время установлено некорректно

        Примеры:
        >>> clock = Clock("Casio", "электронные", 10, 30)
        >>> clock.set_time(15, 45)
        """
        ...

    def add_minutes(self, minutes: int) -> None:
        """
        Добавление минут к текущему времени.

        :param minutes: Количество минут для добавления
        :raise TypeError: Если количество минут не является целым числом
        :raise ValueError: Если количество минут отрицательное

        Примеры:
        >>> clock = Clock("Casio", "электронные", 10, 30)
        >>> clock.add_minutes(25)
        """
        ...

    def get_time(self) -> str:
        """
        Получение текущего времени в формате строки.

        :return: Время в формате "ЧЧ:ММ"

        Примеры:
        >>> clock = Clock("Casio", "электронные", 14, 20)
        >>> clock.get_time()
        '14:20'
        """
        ...


class Headphones:
    """
    Класс, представляющий наушники.

    Attributes:
        brand (str): Бренд наушников
        type (str): Тип наушников (накладные, внутриканальные, беспроводные)
        is_on (bool): Включены ли наушники
    """

    def __init__(self, brand: str, type: str, is_on: bool = False):
        """
        Создание и подготовка к работе объекта "Наушники"

        :param brand: Бренд наушников
        :param type: Тип наушников
        :param is_on: Начальное состояние наушников

        :raise TypeError: Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если тип наушников не поддерживается

        Примеры:
        >>> headphones = Headphones("Sony", "беспроводные", False)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not isinstance(type, str):
            raise TypeError("Тип наушников должен быть строкой")
        if not isinstance(is_on, bool):
            raise TypeError("Состояние наушников должно быть булевым значением")

        valid_types = ["накладные", "внутриканальные", "беспроводные", "проводные"]
        if type not in valid_types:
            raise ValueError(f"Тип наушников должен быть одним из: {', '.join(valid_types)}")

        self.brand = brand
        self.type = type
        self.is_on = is_on

    def turn_on(self) -> None:
        """
        Включение наушников.

        Примеры:
        >>> headphones = Headphones("Sony", "беспроводные", False)
        >>> headphones.turn_on()
        """
        ...

    def turn_off(self) -> None:
        """
        Выключение наушников.

        Примеры:
        >>> headphones = Headphones("Sony", "беспроводные", True)
        >>> headphones.turn_off()
        """
        ...

    def adjust_volume(self, volume_level: int) -> None:
        """
        Регулировка громкости наушников.

        :param volume_level: Уровень громкости (0-100)
        :raise TypeError: Если уровень громкости не является целым числом
        :raise ValueError: Если уровень громкости вне диапазона 0-100

        Примеры:
        >>> headphones = Headphones("Sony", "беспроводные", True)
        >>> headphones.adjust_volume(75)
        """
        ...


class Car:
    """
    Класс, представляющий автомобиль.

    Attributes:
        brand (str): Марка автомобиля
        model (str): Модель автомобиля
        year (int): Год выпуска
        fuel_level (float): Уровень топлива в процентах (0-100)
    """

    def __init__(self, brand: str, model: str, year: int, fuel_level: float = 100.0):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param year: Год выпуска
        :param fuel_level: Начальный уровень топлива (0-100)

        :raise TypeError: Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если год или уровень топлива некорректны

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022, 80.5)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом")
        if not isinstance(fuel_level, (int, float)):
            raise TypeError("Уровень топлива должен быть числом")
        if year < 1886:
            raise ValueError("Год выпуска должен быть не меньше 1886")
        if fuel_level < 0 or fuel_level > 100:
            raise ValueError("Уровень топлива должен быть от 0 до 100%")

        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_level = float(fuel_level)

    def start_engine(self) -> None:
        """
        Запуск двигателя автомобиля.

        :raise RuntimeError: Если уровень топлива равен нулю

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022, 50.0)
        >>> car.start_engine()
        """
        ...

    def stop_engine(self) -> None:
        """
        Остановка двигателя автомобиля.

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022, 50.0)
        >>> car.stop_engine()
        """
        ...

    def refuel(self, amount: float) -> None:
        """
        Заправка автомобиля.

        :param amount: Количество топлива для заправки в процентах
        :raise TypeError: Если количество топлива не является числом
        :raise ValueError: Если количество топлива отрицательное

        Примеры:
        >>> car = Car("Toyota", "Camry", 2022, 30.0)
        >>> car.refuel(40.0)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()