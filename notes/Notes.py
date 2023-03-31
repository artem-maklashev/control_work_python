from notes.data import Note


class Notes:
    # __notes_list: list[Note] = []

    def __init__(self, notes_list=None):
        if notes_list is None:
            notes_list: list[Note] = []
        self.__notes_list = notes_list

    def add__note(self, my__note: Note):
        self.__notes_list.append(my__note)

    def delete__note(self, index: int):
        self.__notes_list.pop(index)

    def get__note(self, index):
        return self.__notes_list[index]

    @property
    def notes(self):
        return self.__notes_list

    def to_dict(self):
        my_dict = {}
        for note in self.__notes_list:
            my_dict[note.get_id] = note.__dict__
        return my_dict

    @property
    def size(self):
        return len(self.__notes_list)


    @staticmethod
    def to_notes(data):
        notes_list = []
        for item in data:
            note = Note()
            note.id = item["_Note__id"]
            note.c_date = item["_Note__note_creation_date"]
            note.text = item["_Note__note_text"]
            note.e_date = item["_Note__note_creation_date"]
            note.header = item["_Note__note_header"]
            notes_list.append(note)
        notes = Notes(notes_list)
        return notes
