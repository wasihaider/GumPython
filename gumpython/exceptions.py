class GumPythonError(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"


class InputError(GumPythonError):
    pass


class BorderInputError(InputError):
    pass


class ColorInputError(InputError):
    pass
