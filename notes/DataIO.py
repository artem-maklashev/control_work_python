from abc import ABC, abstractmethod
from notes.Notes import Notes
from presenter.Presenter import Presenter


class DataIO(ABC):

    def __init__(self):
        self.presenter = None

    @abstractmethod
    def load_data(self) -> Notes:
        """загрузка из файла"""

    @abstractmethod
    def save_data(self):
        """Сохранение в файл"""

    @abstractmethod
    def set_presenter(self, presenter: Presenter):
        """Устанавливаем презентер"""
