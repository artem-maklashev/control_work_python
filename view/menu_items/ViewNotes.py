from view.menu_items.MenuMethods import MenuMethods


class ViewNotes(MenuMethods):
    def description(self):
        return "Просмотреть записи"

    def run(self):
        self.get_ui().show_notes()
