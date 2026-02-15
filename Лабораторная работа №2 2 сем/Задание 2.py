BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """Класс для представления книги"""

    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация экземпляра класса Book

        Args:
            id_: идентификатор книги
            name: название книги
            pages: количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Возвращает строковое представление книги"""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Возвращает валидную Python строку для создания такого же экземпляра"""
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    """Класс для представления библиотеки"""

    def __init__(self, books=None):
        """
        Инициализация экземпляра класса Library

        Args:
            books: список книг (по умолчанию None - создается пустой список)
        """
        if books is None:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги в библиотеку

        Returns:
            int: следующий доступный id для книги
        """
        if not self.books:  # если список книг пуст
            return 1
        else:
            # возвращаем id последней книги + 1
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её идентификатору

        Args:
            book_id: идентификатор книги

        Returns:
            int: индекс книги в списке

        Raises:
            ValueError: если книги с указанным id не существует
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index

        # если книга не найдена
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))