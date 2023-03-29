from notes.Notes import Notes
from notes.data.FormatJson import FormatJson
from presenter.Presenter import Presenter
from view.ConsoleUI import ConsoleUI

view = ConsoleUI()
notes = Notes()
data_io = FormatJson()
presenter = Presenter(view, notes, data_io)
view.start()
