from notes import DataIO
from notes.Notes import Notes
from notes.data.Note import Note
from view.View import View


class Presenter:
    __notes = Notes()

    def __init__(self, view: View, notes: Notes, data_io: DataIO):
        self.__notes = notes
        self.__view = view
        self.__data_io = data_io
        self.__notes = self.__data_io.load_data(self)
        print(self.__notes)
        view.set_presenter(self)

    @property
    def get_notes(self):
        return self.__notes

    def print_exception(self, text: str):
        self.__view.message(text)

    def add_note(self, note: Note):
        self.__notes.append(note)

    def exit(self):
        # for note in self.__notes:
        #     print(n)
        self.__data_io.save_data(self)