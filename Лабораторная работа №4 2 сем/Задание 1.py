from abc import ABC, abstractmethod
from typing import Optional


class Vehicle(ABC):
    """
    Базовый класс для всех транспортных средств.

    Атрибуты:
        _brand (str): Марка транспортного средства (непубличный, для защиты от прямого изменения)
        _model (str): Модель транспортного средства (непубличный)
        _year (int): Год выпуска (непубличный)
        _mileage (float): Пробег в км (непубличный, изменяется только через методы)
    """

    def __init__(self, brand: str, model: str, year: int, mileage: float = 0.0) -> None:
        """
        Инициализация транспортного средства.

        Args:
            brand: Марка автомобиля
            model: Модель автомобиля
            year: Год выпуска
            mileage: Начальный пробег (по умолчанию 0)
        """
        self._brand = brand
        self._model = model
        self._year = year
        self._mileage = mileage

    def __str__(self) -> str:
        """Возвращает удобочитаемое строковое представление."""
        return f"{self._brand} {self._model} ({self._year})"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление для отладки."""
        return f"{self.__class__.__name__}(brand='{self._brand}', model='{self._model}', year={self._year}, mileage={self._mileage})"

    def drive(self, distance: float) -> None:
        """
        Увеличивает пробег автомобиля.

        Args:
            distance: Пройденное расстояние в км

        Raises:
            ValueError: Если distance отрицательное
        """
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        self._mileage += distance
        print(f"Проехали {distance} км. Общий пробег: {self._mileage} км")

    def get_mileage(self) -> float:
        """Возвращает текущий пробег (геттер для защищенного атрибута)."""
        return self._mileage

    @abstractmethod
    def calculate_fuel_efficiency(self) -> float:
        """
        Абстрактный метод для расчета эффективности расхода топлива.
        Должен быть переопределен в дочерних классах.

        Returns:
            float: Расход топлива в литрах на 100 км
        """
        pass


class PassengerCar(Vehicle):
    """
    Класс легкового автомобиля, наследующий Vehicle.

    Дополнительные атрибуты:
        _passenger_capacity (int): Вместимость пассажиров (непубличный)
    """

    def __init__(self, brand: str, model: str, year: int, passenger_capacity: int, mileage: float = 0.0) -> None:
        """
        Расширение конструктора базового класса.

        Args:
            brand: Марка автомобиля
            model: Модель автомобиля
            year: Год выпуска
            passenger_capacity: Количество пассажирских мест
            mileage: Начальный пробег
        """
        super().__init__(brand, model, year, mileage)
        self._passenger_capacity = passenger_capacity

    def __str__(self) -> str:
        """Перегрузка метода __str__ для добавления информации о вместимости."""
        return f"{super().__str__()}, вместимость: {self._passenger_capacity} чел."

    def calculate_fuel_efficiency(self) -> float:
        """
        Реализация абстрактного метода для легкового автомобиля.

        Returns:
            float: Расход топлива ~8 л/100км (усредненно)
        """
        base_consumption = 8.0
        age_factor = (2024 - self._year) * 0.1
        return base_consumption + age_factor

    def drive(self, distance: float) -> None:
        """
        Перегрузка метода drive с дополнительной проверкой.

        Причина перегрузки: для легковых автомобилей важно учитывать,
        что при перевозке пассажиров расход топлива увеличивается.

        Args:
            distance: Пройденное расстояние
        """
        super().drive(distance)
        if self._mileage > 0:
            print(f"Рекомендуемая проверка давления в шинах через {10000 - (self._mileage % 10000)} км")


class Truck(Vehicle):
    """
    Класс грузового автомобиля, наследующий Vehicle.

    Дополнительные атрибуты:
        _load_capacity (float): Грузоподъемность в тоннах (непубличный)
        _current_load (float): Текущая загрузка в тоннах (непубличный)
    """

    def __init__(self, brand: str, model: str, year: int, load_capacity: float, mileage: float = 0.0) -> None:
        """
        Расширение конструктора базового класса.

        Args:
            brand: Марка автомобиля
            model: Модель автомобиля
            year: Год выпуска
            load_capacity: Грузоподъемность в тоннах
            mileage: Начальный пробег
        """
        super().__init__(brand, model, year, mileage)
        self._load_capacity = load_capacity
        self._current_load = 0.0

    def __repr__(self) -> str:
        """Перегрузка __repr__ для включения информации о грузоподъемности."""
        return (f"{self.__class__.__name__}(brand='{self._brand}', model='{self._model}', "
                f"year={self._year}, load_capacity={self._load_capacity}, mileage={self._mileage})")

    def calculate_fuel_efficiency(self) -> float:
        """
        Реализация абстрактного метода для грузового автомобиля.

        Returns:
            float: Расход топлива в зависимости от загрузки
        """
        base_consumption = 25.0
        load_factor = (self._current_load / self._load_capacity) * 10 if self._load_capacity > 0 else 0
        return base_consumption + load_factor

    def load_cargo(self, weight: float) -> None:
        """
        Загрузка груза (новый метод, специфичный для грузовиков).

        Args:
            weight: Вес груза в тоннах

        Raises:
            ValueError: Если превышена грузоподъемность или вес отрицательный
        """
        if weight < 0:
            raise ValueError("Вес груза не может быть отрицательным")
        if self._current_load + weight > self._load_capacity:
            raise ValueError(f"Превышение грузоподъемности! Максимум: {self._load_capacity} т")

        self._current_load += weight
        print(f"Загружено {weight} т. Текущая загрузка: {self._current_load}/{self._load_capacity} т")

    def drive(self, distance: float) -> None:
        """
        Перегрузка метода drive с учетом загрузки.

        Причина перегрузки: для грузовых автомобилей критично знать загрузку
        для расчета износа и безопасности движения.

        Args:
            distance: Пройденное расстояние
        """
        if self._current_load == 0:
            print("Внимание: движение порожнего грузовика!")

        super().drive(distance)

        if self._current_load > self._load_capacity * 0.9:
            print("Работа с максимальной загрузкой. Рекомендуется снизить скорость.")

if __name__ == "__main__":
    car = PassengerCar("Toyota", "Camry", 2020, 5, 15000)
    truck = Truck("Volvo", "FH16", 2019, 20.0, 50000)


    print(car)
    print(repr(car))

    car.drive(100)
    print(f"Эффективность: {car.calculate_fuel_efficiency():.2f} л/100км")

    truck.load_cargo(15.0)
    truck.drive(200)
    print(f"Эффективность грузовика: {truck.calculate_fuel_efficiency():.2f} л/100км")