from gumpython.flags import (
    ChooseCursorFlag,
    ChooseItemFlag,
    ChooseListFlag,
    ChooseSelectedFlag,
    ConfirmGeneralFlag,
    ConfirmPromptFlag,
    ConfirmSelectedFlag,
    ConfirmUnselectedFlag,
    FilterGeneralFlag,
    FilterIndicatorFlag,
    FilterMatchFlag,
    FilterPromptFlag,
    FilterTextFlag,
    FormatFlag,
    InputCursorFlag,
    InputGeneralFlag,
    InputPromptFlag,
    JoinTextFlag,
    SpinnerFlag,
    SpinnerTitleFlag,
    SpinSpinnerFlag,
    StyleFlag,
)


class Argument:
    pass


class StyleArgument(Argument):
    def __init__(self):
        self.args = StyleFlag()


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


class FilterArguments(Argument):
    def __init__(self):
        self.general = FilterGeneralFlag()
        self.match = FilterMatchFlag()
        self.prompt = FilterPromptFlag()
        self.indicator = FilterIndicatorFlag()
        self.text = FilterTextFlag()


class FormatArguments(Argument):
    def __init__(self):
        self.type = FormatFlag()


class InputArguments(Argument):
    def __init__(self):
        self.general = InputGeneralFlag()
        self.cursor = InputCursorFlag()
        self.prompt = InputPromptFlag()


class JoinArguments(Argument):
    def __init__(self):
        self.text = JoinTextFlag()


class SpinArguments(Argument):
    def __init__(self):
        self.general = SpinnerFlag()
        self.spinner = SpinSpinnerFlag()
        self.title = SpinnerTitleFlag()
