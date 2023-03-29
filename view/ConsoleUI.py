from notes.data.Note import Note
from view.Menu import Menu
from view import Validator
from view.View import View
from view.menu_items.AddNote import AddNote
from view.menu_items.Exit import Exit
from view.menu_items.ViewNotes import ViewNotes


class ConsoleUI(View):
    def add_note(self):
        note = Note()
        note.header = input("Введите заголовок заметки")
        note.text = input("Введите текст заметки")
        self.__presenter.add_note(note)

    def message(self, text):
        print(text)

    def __init__(self):
        self.__presenter = None
        self.__flag_run = True

    def set_presenter(self, presenter):
        self.__presenter = presenter

    def start(self):
        menu = Menu(self)
        menu.add_item(ViewNotes(self))
        menu.add_item(AddNote(self))
        menu.add_item(Exit(self))
        while self.__flag_run:
            print(menu.print_menu())
            selection = input("Выберите пункт меню\n")
            if Validator.is_valid(selection, menu):
                menu.run(int(selection)-1)

    def exit(self):
        self.__presenter.exit()
        self.__flag_run = False

    def show_notes(self):
        notes = self.__presenter.get_notes
        for note in notes:
            print(f"{note.get_id} |"
                  f"{note.creation_date} |"
                  f"{note.edit_date} |"
                  f"{note.header} |"
                  f"{note.text}\n")
