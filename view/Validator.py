from view.Menu import Menu


def is_valid(text: str, size: int):
    if text.isdigit():
        if int(text)-1 < size and int(text) > 0:
            return True
    else:
        return False


