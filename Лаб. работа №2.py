from typing import List, Optional


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        # Присвоение значений атрибутам объекта
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        # Возврат названия книги в кавычках
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        # Возврат python-строки для воссоздания объекта
        return f"Book(id_={self.id_}, name={self.name!r}, pages={self.pages})"


class Library:
    def __init__(self, books: Optional[List[Book]] = None):
        # Инициализация списка книг (пустой список по умолчанию)
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        # Расчет id для новой книги на основе последнего элемента
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        # Поиск индекса книги по ее идентификатору
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index

        # Генерация ошибки при отсутствии книги в списке
        raise ValueError("Книги с запрашиваемым id не существует")