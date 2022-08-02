from .inputs import Input
from gumpython.exceptions import BorderInputError


class BorderType:
    NONE = "none"
    HIDDEN = "hidden"
    NORMAL = "normal"
    ROUNDED = "rounded"
    THICK = "thick"
    DOUBLE = "double"


def all_border_types():
    return [
        BorderType.NONE,
        BorderType.HIDDEN,
        BorderType.NORMAL,
        BorderType.ROUNDED,
        BorderType.THICK,
        BorderType.DOUBLE,
    ]


class Border(Input):
    def __init__(self, border_type):
        self.border_type = border_type

    def is_valid(self):
        return self._validate()

    def _validate(self):
        if not isinstance(self.border_type, str):
            raise BorderInputError(f"'str' input expected '{type(self.border_type).__name__}' given")
        if self.border_type not in all_border_types():
            raise BorderInputError(f"border must be one of {all_border_types()} but got '{self.border_type}'")
        return True

    def compile(self):
        return self.border_type
