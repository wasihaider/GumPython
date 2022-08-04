class GumPythonError(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"


class GumNotFoundError(GumPythonError):
    pass


class ArgumentError(GumPythonError):
    pass


class StyleArgumentError(ArgumentError):
    pass


class ChooseArgumentError(ArgumentError):
    pass


class InputError(GumPythonError):
    pass


class BorderInputError(InputError):
    pass


class ColorInputError(InputError):
    pass


class PositionInputError(InputError):
    pass


class AlignmentInputError(InputError):
    pass
