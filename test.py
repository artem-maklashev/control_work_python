import json
from notes.Notes import Notes
from notes.data.Note import Note

note = Note("тест", "какой то текст")
note2 = Note("another one", "some note")
notes = Notes()
notes.add__note(note)
notes.add__note(note2)

try:
    with open("test.json", 'w', encoding='utf-8') as data_file:

        string = json.dumps(notes.notes, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
        print(string)
        json.dump(notes.notes, data_file, default=lambda o: o.__dict__, sort_keys=True, indent=4, ensure_ascii=False)
        # str1 = json.dumps(notes, cls=NotesEncoder)
        # print(str1)
        # presenter.print_exception("Файл сохранен")
        data_file.close()
except IOError:
    # presenter.print_exception("Не удалось сохранить файл")
    print("не удалось сохранить файл")

# with open("test.json", 'r', encoding='utf-8') as data_file:
#     user_object = json.load(data_file)
#     print(json.dumps(user_object, ensure_ascii=False))

def to_notes(user_object):
    notes_list = []
    for item in user_object:
        note = Note()
        note.id = item["_Note__id"]
        note.c_date = item["_Note__note_creation_date"]
        note.text = item["_Note__note_text"]
        note.e_date = item["_Note__note_creation_date"]
        note.header = item["_Note__note_header"]
        notes_list.append(note)
    notes_new = Notes(notes_list)
    return notes_new


with open("test.json", 'r', encoding='utf-8') as data_file:
    # user_object = json.load(data_file, object_hook=lambda d: SimpleNamespace(**d))
    user_object = json.load(data_file)
    print("*************************")
    print(user_object)
    notes = to_notes(user_object)
    print(notes)
    for note in notes.notes:
        print(note)

