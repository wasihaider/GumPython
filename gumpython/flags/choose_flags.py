from gumpython.constants import FlagSeparatorChoice, FlagTypeChoice

from .flags import BaseFlag, Flag, SubFlag


class ChooseCursorFlag(BaseFlag):
    def __init__(self):
        super().__init__()
        # main
        self.cursor = Flag(name=self.flag_name, type=FlagTypeChoice.STR)
        self.prefix = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.STR,
            sub_name="prefix",
            separator=FlagSeparatorChoice.HYPHEN,
        )

    def get_flag_name(self):
        return "cursor"


class ChooseItemFlag(BaseFlag):
    def __init__(self):
        super(ChooseItemFlag, self).__init__()

    def get_flag_name(self):
        return "item"


class ChooseSelectedFlag(BaseFlag):
    def __init__(self):
        super(ChooseSelectedFlag, self).__init__()
        self.prefix = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.STR,
            sub_name="prefix",
            separator=FlagSeparatorChoice.HYPHEN,
        )

    def get_flag_name(self):
        return "selected"


class ChooseListFlag:
    def __init__(self):
        self.height = Flag(name="height", type=FlagTypeChoice.INT)
        self.limit = Flag(name="limit", type=FlagTypeChoice.INT)
        self.no_limit = Flag(name="no-limit", type=FlagTypeChoice.BOOL)
        self.unselected_prefix = Flag(
            name="unselected-prefix", type=FlagTypeChoice.STR
        )
