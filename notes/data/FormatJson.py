import json

import config
from notes.DataIO import DataIO
from notes.Notes import Notes
from notes.data.Note import Note
from presenter.Presenter import Presenter


def to_notes(user_object):
    notes_list = []
    # data = user_object["_Notes__notes_list"]
    for item in user_object:
        note = Note()
        note.id = item["_Note__id"]
        note.c_date = item["_Note__note_creation_date"]
        note.text = item["_Note__note_text"]
        note.e_date = item["_Note__note_edit_date"]
        note.header = item["_Note__note_header"]
        notes_list.append(note)
    notes_new = Notes(notes_list)
    return notes_new


class FormatJson(DataIO):
    _file_name = config.json_file_name

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter: Presenter):
        self.presenter = presenter

    def load_data(self) -> Notes:
        notes = Notes()
        try:
            with open(self._file_name, 'r', encoding='utf-8') as data_file:
                data = json.load(data_file)
                notes = to_notes(data)
        except Exception as e:
            self.presenter.print_exception(f"Файл {self._file_name} не найден\n"
                                           f"{e}")
        return notes

    def save_data(self):

        try:
            with open(self._file_name, 'w', encoding='utf-8') as data_file:
                notes = self.presenter.get_notes
                json.dump(notes.notes, data_file, default=lambda o: o.__dict__, sort_keys=True, indent=4,
                          ensure_ascii=False)
        except Exception as e:
            self.presenter.print_exception(f"не удалось сохранить файл,\n{e}")
