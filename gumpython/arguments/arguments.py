from gumpython.flags import (
    ChooseCursorFlag,
    ChooseItemFlag,
    ChooseListFlag,
    ChooseSelectedFlag,
    ConfirmGeneralFlag,
    ConfirmPromptFlag,
    ConfirmSelectedFlag,
    ConfirmUnselectedFlag,
    StyleBorderFlag,
    StyleTextFlag,
)


class Argument:
    pass


class StyleArgument(Argument):
    def __init__(self):
        self.border = StyleBorderFlag()
        self.text = StyleTextFlag()


class ChooseArgument(Argument):
    def __init__(self):
        self.cursor = ChooseCursorFlag()
        self.item = ChooseItemFlag()
        self.selected = ChooseSelectedFlag()
        self.list = ChooseListFlag()


class ConfirmArguments(Argument):
    def __init__(self):
        self.general = ConfirmGeneralFlag()
        self.prompt = ConfirmPromptFlag()
        self.selected = ConfirmSelectedFlag()
        self.unselected = ConfirmUnselectedFlag()
