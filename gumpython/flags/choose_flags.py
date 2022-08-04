from gumpython.constants import FlagSeparatorChoice, FlagTypeChoice

from .flags import Flag, SubFlag


class ChooseFlag:
    def __init__(self):
        self.cursor_flag_name = "cursor"


class ChooseCursorFlag(ChooseFlag):
    def __init__(self):
        super().__init__()
        # main
        self.cursor = Flag(name=self.cursor_flag_name, type=FlagTypeChoice.STR)
        self.prefix = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.STR,
            sub_name="prefix",
            separator=FlagSeparatorChoice.HYPHEN,
        )

        # align
        self.align = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.ALIGN,
            sub_name="align",
            separator=FlagSeparatorChoice.DOT,
        )
        self.margin = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.POSITION,
            sub_name="margin",
            separator=FlagSeparatorChoice.DOT,
        )
        self.padding = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.POSITION,
            sub_name="padding",
            separator=FlagSeparatorChoice.DOT,
        )

        # color
        self.background = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.COLOR,
            sub_name="background",
            separator=FlagSeparatorChoice.DOT,
        )
        self.foreground = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.COLOR,
            sub_name="foreground",
            separator=FlagSeparatorChoice.DOT,
        )

        # style
        self.bold = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.BOOL,
            sub_name="bold",
            separator=FlagSeparatorChoice.DOT,
        )
        self.faint = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.BOOL,
            sub_name="faint",
            separator=FlagSeparatorChoice.DOT,
        )
        self.italic = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.BOOL,
            sub_name="italic",
            separator=FlagSeparatorChoice.DOT,
        )
        self.strikethrough = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.BOOL,
            sub_name="strikethrough",
            separator=FlagSeparatorChoice.DOT,
        )
        self.underline = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.BOOL,
            sub_name="underline",
            separator=FlagSeparatorChoice.DOT,
        )

        # border
        self.border = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.BORDER,
            sub_name="border",
            separator=FlagSeparatorChoice.DOT,
        )
        self.border_background = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.COLOR,
            sub_name="border-background",
            separator=FlagSeparatorChoice.DOT,
        )
        self.border_foreground = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.COLOR,
            sub_name="border-foreground",
            separator=FlagSeparatorChoice.DOT,
        )

        # size
        self.height = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.INT,
            sub_name="height",
            separator=FlagSeparatorChoice.DOT,
        )
        self.width = SubFlag(
            name=self.cursor_flag_name,
            type=FlagTypeChoice.INT,
            sub_name="width",
            separator=FlagSeparatorChoice.DOT,
        )
