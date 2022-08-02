from gumpython.flags import ChooseCursorFlag, StyleBorderFlag, StyleTextFlag


class Argument:
    pass


class StyleArgument(Argument):
    def __init__(self):
        self.border = StyleBorderFlag()
        self.text = StyleTextFlag()


class ChooseArgument(Argument):
    def __init__(self):
        self.cursor = ChooseCursorFlag()
