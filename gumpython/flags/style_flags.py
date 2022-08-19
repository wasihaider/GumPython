from gumpython.constants import FlagSeparatorChoice, FlagTypeChoice

from .flags import Flag, SubFlag


class StyleFlag:
    def __init__(self):
        self.border = Flag(name="border", type=FlagTypeChoice.BORDER)
        self.border_background = SubFlag(
            name="border",
            type=FlagTypeChoice.COLOR,
            sub_name="background",
            separator=FlagSeparatorChoice.HYPHEN,
        )
        self.border_foreground = SubFlag(
            name="border",
            type=FlagTypeChoice.COLOR,
            sub_name="foreground",
            separator=FlagSeparatorChoice.HYPHEN,
        )
        self.align = Flag(name="align", type=FlagTypeChoice.ALIGN)
        self.background = Flag(name="background", type=FlagTypeChoice.COLOR)
        self.foreground = Flag(name="foreground", type=FlagTypeChoice.COLOR)
        self.bold = Flag(name="bold", type=FlagTypeChoice.BOOL)
        self.faint = Flag(name="faint", type=FlagTypeChoice.BOOL)
        self.height = Flag(name="height", type=FlagTypeChoice.INT)
        self.italic = Flag(name="italic", type=FlagTypeChoice.BOOL)
        self.strikethrough = Flag(
            name="strikethrough", type=FlagTypeChoice.BOOL
        )
        self.underline = Flag(name="underline", type=FlagTypeChoice.BOOL)
        self.margin = Flag(name="margin", type=FlagTypeChoice.POSITION)
        self.padding = Flag(name="padding", type=FlagTypeChoice.POSITION)
        self.width = Flag(name="width", type=FlagTypeChoice.INT)
