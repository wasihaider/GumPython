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
    style = Flag(
        name="border",
        type=FlagType(name=FlagTypeChoice.COLOR),
        default="none"
    )
    background_color = SubFlag(
        name="border",
        type=FlagType(name=FlagTypeChoice.COLOR),
        sub_name="background",
        separator=FlagSeparatorChoice.HYPHEN
    )
    foreground_color = SubFlag(
        name="border",
        type=FlagType(name=FlagTypeChoice.COLOR),
        sub_name="foreground",
        separator=FlagSeparatorChoice.HYPHEN
    )
