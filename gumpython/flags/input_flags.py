from gumpython.constants import FlagTypeChoice

from .flags import BaseFlag, Flag


class InputCursorFlag(BaseFlag):
    def __init__(self):
        super(InputCursorFlag, self).__init__()

    def get_flag_name(self):
        return "cursor"


class InputPromptFlag(BaseFlag):
    def __init__(self):
        super(InputPromptFlag, self).__init__()
        self.prompt = Flag(name=self.flag_name, type=FlagTypeChoice.STR)

    def get_flag_name(self):
        return "prompt"


class InputGeneralFlag:
    def __init__(self):
        self.char_limit = Flag(name="char-limit", type=FlagTypeChoice.INT)
        self.password = Flag(name="password", type=FlagTypeChoice.BOOL)
        self.placeholder = Flag(name="placeholder", type=FlagTypeChoice.STR)
        self.value = Flag(name="value", type=FlagTypeChoice.STR)
        self.width = Flag(name="width", type=FlagTypeChoice.INT)
