from datetime import datetime
import itertools


class Note:
    __note_id = itertools.count(1)

    def __init__(self, header=None, text=None):
        self.__id = next(Note.__note_id)
        self.__note_header = header
        self.__note_text = text
        self.__note_creation_date = datetime.now()
        self.__note_edit_date = None

    def __str__(self):
        return (f"id:\t\t {self.__id}\n"
                f"header:\t\t {self.__note_header}\n"
                f"text:\t\t {self.__note_text}\n"
                f"creation date:\t {self.__note_creation_date}\n"
                f"edit date:\t\t {self.__note_edit_date}")

    @property
    def header(self):
        return self.__note_header

    @header.setter
    def header(self, header: str):
        self.__note_header = header


notes = []

note = Note("Header 1")

note2 = Note(text="text")

notes.append(note)
notes.append(note2)
for n in notes:
    print(n)
