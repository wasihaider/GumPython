from gumpython.constants import FlagTypeChoice

from .flags import BaseFlag, Flag


class FilterIndicatorFlag(BaseFlag):
    def __init__(self):
        super(FilterIndicatorFlag, self).__init__()
        self.indicator = Flag(name=self.flag_name, type=FlagTypeChoice.STR)

    def get_flag_name(self):
        return "indicator"


class FilterMatchFlag(BaseFlag):
    def __init__(self):
        super(FilterMatchFlag, self).__init__()

    def get_flag_name(self):
        return "match"


class FilterPromptFlag(BaseFlag):
    def __init__(self):
        super(FilterPromptFlag, self).__init__()
        self.prompt = Flag(name=self.flag_name, type=FlagTypeChoice.STR)

    def get_flag_name(self):
        return "prompt"


class FilterTextFlag(BaseFlag):
    def __init__(self):
        super(FilterTextFlag, self).__init__()

    def get_flag_name(self):
        return "text"


class FilterGeneralFlag:
    def __init__(self):
        self.height = Flag(name="height", type=FlagTypeChoice.INT)
        self.placeholder = Flag(name="placeholder", type=FlagTypeChoice.STR)
        self.width = Flag(name="width", type=FlagTypeChoice.INT)
