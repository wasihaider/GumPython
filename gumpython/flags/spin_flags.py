from gumpython.constants import FlagTypeChoice

from .flags import BaseFlag, Flag


class SpinSpinnerFlag(BaseFlag):
    def __init__(self):
        super(SpinSpinnerFlag, self).__init__()
        self.spinner = Flag(name=self.flag_name, type=FlagTypeChoice.SPINNER)

    def get_flag_name(self):
        return "spinner"


class SpinnerTitleFlag(BaseFlag):
    def __init__(self):
        super(SpinnerTitleFlag, self).__init__()
        self.title = Flag(name=self.flag_name, type=FlagTypeChoice.STR)

    def get_flag_name(self):
        return "title"


class SpinnerFlag:
    def __init__(self):
        self.show_output = Flag(name="show-output", type=FlagTypeChoice.BOOL)
