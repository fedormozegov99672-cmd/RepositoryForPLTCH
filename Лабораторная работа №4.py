from typing import Optional


class Textbook:
    """ Базовый класс для печатных учебников """

    def __init__(self, title: str, subject: str, amount: int):
        self.title = title
        self.subject = subject
        # Инкапсуляция: скрываем количество, чтобы изменять
        # его только через метод выдачи (защита данных).
        self._amount = amount

    def take_book(self) -> None:
        """ Метод для выдачи учебника на руки """
        if self._amount > 0:
            self._amount -= 1
            print(f"Учебник '{self.title}' выдан. Осталось в шкафу: {self._amount}")
        else:
            print(f"Ошибка: учебник '{self.title}' закончился.")

    def __str__(self) -> str:
        return f"Учебник по {self.subject}: {self.title}"

    def __repr__(self) -> str:
        return f"Textbook(title='{self.title}', amount={self._amount})"


class DigitalTextbook(Textbook):
    """ Дочерний класс для электронных пособий (PDF/DJVU) """

    def __init__(self, title: str, subject: str, amount: int, file_format: str):
        # Подтягиваем конструктор родителя
        super().__init__(title, subject, amount)
        self.file_format = file_format

    def get_format(self) -> str:
        """ Уникальный метод для электронки """
        return f"Формат файла: {self.file_format}"

    def take_book(self) -> None:
        """
        Перегрузка метода выдачи.
        Причина: Цифровой учебник не занимает физическое место,
        поэтому мы не уменьшаем поле _amount при 'выдаче'.
        """
        print(f"Ссылка на скачивание '{self.title}' ({self.file_format}) отправлена.")

    def __str__(self) -> str:
        # Полиморфизм: меняем описание под электронку
        return f"[E-LEARNING] {self.title} (Предмет: {self.subject})"

    def __repr__(self) -> str:
        return f"DigitalTextbook(title='{self.title}', format='{self.file_format}')"


if __name__ == "__main__":
    # Обычный учебник
    physics = Textbook("Курс общей физики", "Физика", 10)
    print(physics)
    physics.take_book()

    print("-" * 15)

    # Электронное пособие
    python_lab = DigitalTextbook("Лабораторный практикум", "Программирование", 1, "PDF")
    print(python_lab)
    # Сработает перегруженная логика
    python_lab.take_book()
    print(python_lab.get_format())