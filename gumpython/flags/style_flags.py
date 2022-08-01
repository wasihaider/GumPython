from .flags import (
    Flag,
    FlagType,
    FlagTypeChoice,
    SubFlag,
    FlagSeparatorChoice
)


class StyleFlag:
    pass


class StyleBorderFlag(StyleFlag):
    def __init__(self):
        self.style = Flag(
            name="border",
            type=FlagType(name=FlagTypeChoice.COLOR),
            default="none"
        )
        self.background_color = SubFlag(
            name="border",
            type=FlagType(name=FlagTypeChoice.COLOR),
            sub_name="background",
            separator=FlagSeparatorChoice.HYPHEN
        )
        self.foreground_color = SubFlag(
            name="border",
            type=FlagType(name=FlagTypeChoice.COLOR),
            sub_name="foreground",
            separator=FlagSeparatorChoice.HYPHEN
        )


class StyleTextFlag(StyleFlag):
    def __init__(self):
        self.align = Flag(
            name="align",
            type=FlagType(name=FlagTypeChoice.ALIGN),
            default="left"
        )
        self.background_color = Flag(
            name="background",
            type=FlagType(name=FlagTypeChoice.COLOR)
        )
        self.foreground_color = Flag(
            name="foreground",
            type=FlagType(name=FlagTypeChoice.COLOR)
        )
        self.bold = Flag(
            name="bold",
            type=FlagType(name=FlagTypeChoice.BOOL)
        )
        self.faint = Flag(
            name="faint",
            type=FlagType(name=FlagTypeChoice.BOOL)
        )
        self.height = Flag(
            name="height",
            type=FlagType(name=FlagTypeChoice.INT)
        )
        self.italic = Flag(
            name="italic",
            type=FlagType(name=FlagTypeChoice.BOOL)
        )
        self.strikethrough = Flag(
            name="strikethrough",
            type=FlagType(name=FlagTypeChoice.BOOL)
        )
        self.underline = Flag(
            name="underline",
            type=FlagType(name=FlagTypeChoice.BOOL)
        )
        self.margin = Flag(
            name="margin",
            type=FlagType(name=FlagTypeChoice.POSITION)
        )
        self.padding = Flag(
            name="padding",
            type=FlagType(name=FlagTypeChoice.POSITION)
        )
        self.width = Flag(
            name="width",
            type=FlagType(name=FlagTypeChoice.INT)
        )
