import doctest


class Laptop:
    turn_on: bool = False

    def __init__(self, ram: int, company: str) -> None:
        """
        Конструктор класса ноутбук

        :param ram: количество оперативной памяти
        :param company: имя компании, чей ноутбук

        Примеры:
        >>> laptop = Laptop(16, 'Asus')
        """

        if not isinstance(ram, int):
            raise TypeError('Количество оперативной памяти должно быть целым числом, так как измеряется в Гб')
        if not isinstance(company, str):
            raise TypeError('Название компании должно быть строкой')

        if len(company) < 1 or len(company) > 50:
            raise ValueError('Название компании не может быть пустой строкой и не может превышать 50 символов')
        if (ram and not (ram & ram - 1)) is False:
            raise ValueError('Количество оперативной памяти должно быть степенью 2')

        self.ram = ram
        self.company = company

    def update_ram(self, new_ram: int) -> None:
        """
        Обновить количество оперативной памяти

        :param new_ram: память, которую добавляем
        :return: Сколько сейчас оперативной памяти в ноутбуке

        Примеры:
        >>> laptop = Laptop(16, 'Asus')
        >>> laptop.update_ram(8)
        Теперь в ноутбуке 24Гб оперативной памяти
        """

        if (new_ram and not (new_ram & new_ram - 1)) is False:
            raise ValueError('Новая оперитвка должна быть степенью 2')
        self.ram += new_ram
        print(f"Теперь в ноутбуке {self.ram}Гб оперативной памяти")

    def turn_laptop_on(self) -> None:
        """
        Включить ноутбук

        :return: состояние ноутбука
        Примеры:
        >>> laptop = Laptop(16, 'Asus')
        >>> laptop.turn_laptop_on()
        Ноутбук включен
        """
        self.turn_on = True
        print(f"Ноутбук включен")

    def turn_laptop_off(self) -> None:
        """
        Выключить ноутбук

        :return: состояние ноутбука
        Примеры:
        >>> laptop = Laptop(16, 'Asus')
        >>> laptop.turn_laptop_off()
        Ноутбук выключен
        """
        self.turn_on = True
        print(f"Ноутбук выключен")


if __name__ == '__main__':
    doctest.testmod()
