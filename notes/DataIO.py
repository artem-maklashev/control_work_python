from abc import ABC, abstractmethod

from notes.Notes import Notes
from presenter.Presenter import Presenter


class DataIO(ABC):
    @abstractmethod
    def load_data(self, presenter: Presenter) -> Notes:
        """загрузка из файла"""
    @abstractmethod
    def save_data(self, notes: Notes):
        """Сохранение в файл"""
