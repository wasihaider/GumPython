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


class ConfirmArgumentError(ArgumentError):
    pass


class FilterArgumentError(ArgumentError):
    pass


class FormatArgumentError(ArgumentError):
    pass


class JoinArgumentError(ArgumentError):
    pass


class SpinArgumentError(ArgumentError):
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


class FormatInputError(InputError):
    pass


class SpinnerInputError(InputError):
    pass
