from view.menu_items.MenuMethods import MenuMethods


class DeleteNote(MenuMethods):
    def description(self):
        return "Удалить заметку"

    def run(self):
        self.get_ui().delete_note()