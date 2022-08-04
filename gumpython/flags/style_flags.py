from gumpython.constants import FlagSeparatorChoice, FlagTypeChoice

from .flags import Flag, SubFlag


class StyleFlag:
    pass


class StyleBorderFlag(StyleFlag):
    def __init__(self):
        self.style = Flag(name="border", type=FlagTypeChoice.BORDER)
        self.background_color = SubFlag(
            name="border",
            type=FlagTypeChoice.COLOR,
            sub_name="background",
            separator=FlagSeparatorChoice.HYPHEN,
        )
        self.foreground_color = SubFlag(
            name="border",
            type=FlagTypeChoice.COLOR,
            sub_name="foreground",
            separator=FlagSeparatorChoice.HYPHEN,
        )


class StyleTextFlag(StyleFlag):
    def __init__(self):
        self.align = Flag(name="align", type=FlagTypeChoice.ALIGN)
        self.background_color = Flag(
            name="background", type=FlagTypeChoice.COLOR
        )
        self.foreground_color = Flag(
            name="foreground", type=FlagTypeChoice.COLOR
        )
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
