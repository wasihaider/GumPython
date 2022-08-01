from .inputs import Input


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

    def __validate(self):
        if self.border_type not in all_border_types():
            raise
        return True

    def compile(self):
        return self.border_type
