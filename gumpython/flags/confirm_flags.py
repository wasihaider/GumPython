from gumpython.constants import FlagTypeChoice

from .flags import BaseFlag, Flag


class ConfirmPromptFlag(BaseFlag):
    def __init__(self):
        super(ConfirmPromptFlag, self).__init__()

    def get_flag_name(self):
        return "prompt"


class ConfirmSelectedFlag(BaseFlag):
    def __init__(self):
        super(ConfirmSelectedFlag, self).__init__()

    def get_flag_name(self):
        return "selected"


class ConfirmUnselectedFlag(BaseFlag):
    def __init__(self):
        super(ConfirmUnselectedFlag, self).__init__()

    def get_flag_name(self):
        return "unselected"


class ConfirmGeneralFlag:
    def __init__(self):
        self.affirmative = Flag(name="affirmative", type=FlagTypeChoice.STR)
        self.negative = Flag(name="negative", type=FlagTypeChoice.STR)
