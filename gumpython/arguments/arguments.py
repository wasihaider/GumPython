from gumpython.flags import (
    StyleBorderFlag
)


class Argument:
    pass


class StyleArgument(Argument):
    def __init__(self):
        self.border = StyleBorderFlag()
