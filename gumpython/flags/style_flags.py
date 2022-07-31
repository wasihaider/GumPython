from .flags import (
    Flag,
    FlagType,
    FlagTypeChoice
)


class StyleFlag:
    pass


class StyleBorderFlag(StyleFlag):
    style = Flag(
        name="border",
        type=FlagType(name=FlagTypeChoice.COLOR),
        default="none"
    )
    background_color = Flag(
        name="background",
        type=FlagType(name=FlagTypeChoice.COLOR)
    )
    foreground_color = Flag(
        name="foreground",
        type=FlagType(name=FlagTypeChoice.COLOR)
    )
