import doctest


class Table:
    def __init__(self, length: float, width: float):
        """
        Создание стола с заданными размерами.

        :param length: Длина столешницы
        :param width: Ширина столешницы

        Примеры:
        >>> table = Table(120.5, 60.0)
        """
        if length <= 0 or width <= 0:
            raise ValueError("Размеры стола должны быть положительными")
        self.length = length
        self.width = width

    def get_area(self) -> float:
        """
        Считает площадь поверхности стола.
        :return: Площадь столешницы

        Примеры:
        >>> table = Table(100, 50)
        >>> table.get_area()
        """
        ...

    def move(self, x: float, y: float) -> None:
        """
        Передвинуть стол на новые координаты.
        :param x: Координата X
        :param y: Координата Y
        """
        ...


class ChessPiece:
    def __init__(self, name: str, color: str):
        """
        Создание шахматной фигуры.

        :param name: Название (Пешка, Ферзь и т.д.)
        :param color: Цвет (Белый или Черный)

        Примеры:
        >>> piece = ChessPiece("Пешка", "Белый")
        """
        if not name or not color:
            raise ValueError("Название и цвет должны быть заполнены")
        self.name = name
        self.color = color

    def can_move_to(self, row: int, col: int) -> bool:
        """
        Проверка, может ли фигура пойти на клетку.
        :param row: Номер строки (1-8)
        :param col: Номер столбца (1-8)
        :return: Можно ли сделать ход

        Примеры:
        >>> piece = ChessPiece("Ладья", "Черный")
        >>> piece.can_move_to(4, 5)
        """
        if not (1 <= row <= 8 and 1 <= col <= 8):
            raise ValueError("Координаты должны быть от 1 до 8")
        ...

    def capture(self) -> None:
        """ Снятие фигуры с доски """
        ...


class Backpack:
    def __init__(self, max_weight: float, current_weight: float):
        """
        Рюкзак для вещей.

        :param max_weight: Максимальная нагрузка (кг)
        :param current_weight: Текущий вес вещей внутри

        Примеры:
        >>> bag = Backpack(15.0, 2.5)
        """
        if max_weight <= 0:
            raise ValueError("Максимальный вес должен быть больше нуля")
        if current_weight < 0 or current_weight > max_weight:
            raise ValueError("Вес вещей указан неверно")

        self.max_weight = max_weight
        self.current_weight = current_weight

    def put_item(self, item_weight: float) -> None:
        """
        Положить вещь в рюкзак.
        :param item_weight: Вес вещи
        """
        ...

    def is_overloaded(self) -> bool:
        """ Проверка на перегруз """
        ...


if __name__ == "__main__":
    doctest.testmod()