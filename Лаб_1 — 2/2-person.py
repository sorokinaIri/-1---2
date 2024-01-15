import doctest


class Person:
    def __init__(self, age: int, name: str, surname: str):
        """
        Конструктор класса Персонаж

        :param age: возраст персонажа
        :param name: имя персонажа
        :param surname: фамилия персонажа

        Примеры:
        >>> piter = Person(16, 'Питер', 'Пен')
        """

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not isinstance(surname, str):
            raise TypeError("Фамилия должна быть строкой")

        if (age < 0) or (age > 5000):
            raise ValueError("Возраст должен быть в диапазоне от 0 до 5000 лет")
        if len(name) < 1 or len(name) > 50:
            raise ValueError("Имя не может быть пустой строкой или превышать 50 символов")
        if len(surname) < 1 or len(surname) > 50:
            raise ValueError("Фамилия не может быть пустой строкой или превышать 50 символов")

        self.age = age
        self.name = name
        self.surname = surname

    def greeting(self) -> None:
        """
        Приветствие персонажа

        :return: Вывод приветствия с фамилией и именем персонажа

        Примеры:
        >>> piter = Person(16, 'Питер', 'Пен')
        >>> piter.greeting()
        Привет, я Питер Пен
        """
        print(f"Привет, я {self.name} {self.surname}")

    def get_older(self) -> int:
        """
        Увеличить возраст персонаж на один год

        :return: текующий возраст персонажа

        Примеры:
        >>> piter = Person(16, 'Питер', 'Пен')
        >>> print(piter.get_older())
        17
        """
        self.age += 1
        return self.age


if __name__ == "__main__":
    doctest.testmod()

