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
            type=FlagType(FlagTypeChoice.BORDER),
            default="none"
        )
        self.background_color = SubFlag(
            name="border",
            type=FlagType(FlagTypeChoice.COLOR),
            sub_name="background",
            separator=FlagSeparatorChoice.HYPHEN
        )
        self.foreground_color = SubFlag(
            name="border",
            type=FlagType(FlagTypeChoice.COLOR),
            sub_name="foreground",
            separator=FlagSeparatorChoice.HYPHEN
        )


class StyleTextFlag(StyleFlag):
    def __init__(self):
        self.align = Flag(
            name="align",
            type=FlagType(FlagTypeChoice.ALIGN),
            default="left"
        )
        self.background_color = Flag(
            name="background",
            type=FlagType(FlagTypeChoice.COLOR)
        )
        self.foreground_color = Flag(
            name="foreground",
            type=FlagType(FlagTypeChoice.COLOR)
        )
        self.bold = Flag(
            name="bold",
            type=FlagType(FlagTypeChoice.BOOL)
        )
        self.faint = Flag(
            name="faint",
            type=FlagType(FlagTypeChoice.BOOL)
        )
        self.height = Flag(
            name="height",
            type=FlagType(FlagTypeChoice.INT)
        )
        self.italic = Flag(
            name="italic",
            type=FlagType(FlagTypeChoice.BOOL)
        )
        self.strikethrough = Flag(
            name="strikethrough",
            type=FlagType(FlagTypeChoice.BOOL)
        )
        self.underline = Flag(
            name="underline",
            type=FlagType(FlagTypeChoice.BOOL)
        )
        self.margin = Flag(
            name="margin",
            type=FlagType(FlagTypeChoice.POSITION)
        )
        self.padding = Flag(
            name="padding",
            type=FlagType(FlagTypeChoice.POSITION)
        )
        self.width = Flag(
            name="width",
            type=FlagType(FlagTypeChoice.INT)
        )
