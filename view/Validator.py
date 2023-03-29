from view.Menu import Menu


def is_valid(text: str, menu: Menu):
    if text.isdigit():
        if int(text)-1 < menu.size() and int(text) > 0:
            return True
    else:
        return False


