from view import View
from view.menu_items.MenuItems import MenuItems


class Menu:
    def __init__(self, view: View):
        self.__view = view
        self.__menu_items: list[MenuItems] = []

    def print_menu(self):
        string = ""
        for i in range(len(self.__menu_items)):
            string += f"{i + 1} | {self.__menu_items[i].description()}\n"
        return string

    def add_item(self, new_item: MenuItems):
        self.__menu_items.append(new_item)

    def run(self, index: int):
        menu_item = self.__menu_items[index]
        menu_item.run()

    def size(self):
        return len(self.__menu_items)