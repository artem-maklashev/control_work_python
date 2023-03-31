from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def __init__(self):
        self.__presenter = None

    @abstractmethod
    def set_presenter(self, presenter):
        """Устанавливаем презентер"""

    @abstractmethod
    def start(self):
        """Запуск программы"""
    @abstractmethod
    def message(self, text):
        """Вывод сообщения"""
    @abstractmethod
    def show_notes(self):
        """Показать записи"""
    @abstractmethod
    def add_note(self):
        """Добавить запись"""

    @abstractmethod
    def exit(self):
        """Выход"""
    @abstractmethod
    def edit_note(self):
        """Редактирование заметки"""

    @abstractmethod
    def delete_note(self):
        """Удаление заметки"""
