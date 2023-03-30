from datetime import datetime
import itertools


class Note:
    __note_id = itertools.count(1)

    def __init__(self, header=None, text=None):
        self.__id = next(Note.__note_id)
        self.__note_header = header
        self.__note_text = text
        self.__note_creation_date = datetime.now().strftime("%B %d, %Y")
        self.__note_edit_date = datetime.now().strftime("%B %d, %Y")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def text(self):
        return self.__note_text

    @text.setter
    def text(self, value):
        self.__note_text = value

    @property
    def c_date(self):
        return self.__note_creation_date

    @c_date.setter
    def c_date(self, value):
        self.__note_creation_date = value

    @property
    def e_date(self):
        return self.__note_edit_date

    @e_date.setter
    def e_date(self, value):
        self.__note_edit_date = value

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

    @property
    def get_id(self):
        return self.__id

    @property
    def text(self):
        return self.__note_text

    @text.setter
    def text(self, text):
        self.__note_text = text

    @property
    def creation_date(self):
        return self.__note_creation_date

    @property
    def edit_date(self):
        return self.__note_edit_date

    @edit_date.setter
    def edit_date(self, edit_date):
        self.__note_edit_date = edit_date

    # @staticmethod
    # def from_json(json_dct):
    #     return Note(json_dct['_Note__id'],
    #                 json_dct['_Note__note_creation_date'],
    #                 json_dct['_Note__note_edit_date'],
    #                 json_dct['_Note__note_header'],
    #                 json_dct['_Note__note_text'])
