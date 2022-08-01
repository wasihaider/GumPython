from gumpython.flags import (
    StyleBorderFlag,
    StyleTextFlag
)


class Argument:
    pass


class StyleArgument(Argument):
    def __init__(self):
        self.border = StyleBorderFlag()
        self.text = StyleTextFlag()
