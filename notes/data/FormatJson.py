import json

import config
from notes.DataIO import DataIO
from notes.Notes import Notes
from presenter.Presenter import Presenter


class FormatJson(DataIO):
    _file_name = config.json_file_name

    def load_data(self, notes: Notes) -> Notes:
        data_from_file = []
        try:
            with open(self._file_name, 'r', encoding='utf-8') as data_file:
                data_from_file = json.load(data_file)
                data_file.close()
        except:
            # presenter.print_exception(f"Файл {self._file_name} не найден\n"
            #                           f"Создаю новый файл\n")
            self.save_data(notes=Notes())

        return data_from_file

    def save_data(self, notes: Notes):

        try:
            with open(self._file_name, 'w', encoding='utf-8') as data_file:
                json.dump(notes, data_file, indent=2, ensure_ascii=False)
                # presenter.print_exception("Файл сохранен")
                data_file.close()
        except:
            # presenter.print_exception("Не удалось сохранить файл")
            print("не удалось сохранить файл")
