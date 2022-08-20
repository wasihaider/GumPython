from gumpython.constants import FlagTypeChoice

from .flags import BaseFlag, Flag


class WriteBaseFlag(BaseFlag):
    def __init__(self):
        super(WriteBaseFlag, self).__init__()

    def get_flag_name(self):
        return "base"


class WriteCursorLineNumberFlag(BaseFlag):
    def __init__(self):
        super(WriteCursorLineNumberFlag, self).__init__()

    def get_flag_name(self):
        return "cursor-line-number"


class WriteCursorLineFlag(BaseFlag):
    def __init__(self):
        super(WriteCursorLineFlag, self).__init__()

    def get_flag_name(self):
        return "cursor-line"


class WriteCursorFlag(BaseFlag):
    def __init__(self):
        super(WriteCursorFlag, self).__init__()

    def get_flag_name(self):
        return "cursor"


class WriteEndOfBuffer(BaseFlag):
    def __init__(self):
        super(WriteEndOfBuffer, self).__init__()

    def get_flag_name(self):
        return "end-of-buffer"


class WriteLineNumberFlag(BaseFlag):
    def __init__(self):
        super(WriteLineNumberFlag, self).__init__()

    def get_flag_name(self):
        return "line-number"


class WritePlaceholderFlag(BaseFlag):
    def __init__(self):
        super(WritePlaceholderFlag, self).__init__()
        self.placeholder = Flag(name=self.flag_name, type=FlagTypeChoice.STR)

    def get_flag_name(self):
        return "placeholder"


class WritePromptFlag(BaseFlag):
    def __init__(self):
        super(WritePromptFlag, self).__init__()
        self.prompt = Flag(name=self.flag_name, type=FlagTypeChoice.STR)

    def get_flag_name(self):
        return "prompt"


class WriteGeneralFlag:
    def __init__(self):
        self.char_limit = Flag(name="char-limit", type=FlagTypeChoice.INT)
        self.height = Flag(name="height", type=FlagTypeChoice.INT)
        self.show_cursor_line = Flag(
            name="show-cursor-line", type=FlagTypeChoice.BOOL
        )
        self.show_line_numbers = Flag(
            name="show-line-numbers", type=FlagTypeChoice.BOOL
        )
        self.value = Flag(name="value", type=FlagTypeChoice.STR)
        self.width = Flag(name="width", type=FlagTypeChoice.INT)
