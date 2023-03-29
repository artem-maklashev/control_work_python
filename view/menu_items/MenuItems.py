from abc import ABC, abstractmethod


class MenuItems(ABC):
    @abstractmethod
    def description(self):
        """Описание пункта меню"""

    @abstractmethod
    def run(self):
        """Выполнение пункта меню"""


