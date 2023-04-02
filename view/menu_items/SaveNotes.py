from view.menu_items.MenuMethods import MenuMethods


class SaveNotes(MenuMethods):
    def description(self):
        return "Сохранить заметки"

    def run(self):
        self.get_ui().save_notes()