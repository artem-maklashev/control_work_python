from abc import ABC

from view import View
from view.menu_items.MenuItems import MenuItems


class MenuMethods(MenuItems, ABC):
    def __init__(self, view: View):
        self.__view = view

    def get_ui(self):
        return self.__view
