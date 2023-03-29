from view.menu_items.MenuMethods import MenuMethods


class AddNote(MenuMethods):
    def description(self):
        return "Добавить запись"

    def run(self):
        self.get_ui().add_note()
