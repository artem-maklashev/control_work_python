from notes.data import Note


class Notes:
    notes_list: list[Note] = []

    def __init__(self):
        self.notes_list = []

    def add_note(self, my_note: Note):
        self.notes_list.append(my_note)

    def delete_note(self, index: int):
        self.notes_list.pop(index)

    def get_note(self, index: int):
        return self.notes_list[index]


