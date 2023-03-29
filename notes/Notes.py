from notes.data import Note


class Notes:
    __notes_list: list[Note] = []

    def __init__(self):
        self.__notes_list: list[Note] = []

    def add__note(self, my__note: Note):
        self.__notes_list.append(my__note)

    def delete__note(self, index: int):
        self.__notes_list.pop(index)

    def get__note(self, index: int):
        return self.__notes_list[index]


