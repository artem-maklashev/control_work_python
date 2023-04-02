from datetime import datetime

from notes import DataIO
from notes.Notes import Notes
from notes.data.Note import Note
from view.View import View


class Presenter:
    # __notes = Notes()

    def __init__(self, view: View, notes: Notes, data_io: DataIO):
        self.__notes = notes
        self.__view = view
        self.__data_io = data_io
        data_io.set_presenter(self)
        self.__notes = self.__data_io.load_data()
        view.set_presenter(self)

    def set_edited_flag(self):
        self.__notes.edited_flag_value(True)

    def get_edited_flag(self):
        # print(self.__notes.edited_flag_value)
        return self.__notes.edited_flag_value

    @property
    def get_notes(self):
        return self.__notes

    def print_exception(self, text: str):
        self.__view.message(text)

    def add_note(self, note: Note):
        self.__notes.notes.append(note)

    def save(self):
        self.__data_io.save_data()
        self.__notes.edited_flag_value(False)

    def exit(self):
        self.__data_io.save_data()

    def get_notes_size(self):
        return self.__notes.size

    def get_fields(self, index: int):
        note = self.__notes.get__note(index - 1)
        return note.header, note.text

    def set_fields(self, index: int, header: str, text: str):
        note = self.__notes.get__note(index - 1)
        note.header = header
        note.text = text
        note.edit_date = datetime.now().strftime("%B %d, %Y; %H:%M")

    def delete_note(self, index: int):
        self.__notes.delete__note(index - 1)
