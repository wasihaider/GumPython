from gumpython.arguments import InputArguments

from .command import GumCommand


class Input(GumCommand):
    def __init__(self):
        super(Input, self).__init__()
        self.argument = "input"
        self.arguments = InputArguments()
        self.returning = True

    def run(self):
        response = super(Input, self).run()
        return response[:-1]

    def char_limit(self, limit: int):
        self._add_to_flag_set(self.arguments.general.char_limit, limit)
        return self

    def password(self):
        self._add_to_flag_set(self.arguments.general.password, True)
        return self

    def placeholder(self, placeholder: str):
        self._add_to_flag_set(self.arguments.general.placeholder, placeholder)
        return self

    def value(self, value: str):
        self._add_to_flag_set(self.arguments.general.value, value)
        return self

    def width(self, width: int):
        self._add_to_flag_set(self.arguments.general.width, width)
        return self

    def cursor_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.cursor, alignment, margin, padding)
        return self

    def cursor_color(
        self, foreground_color: str, background_color: str = None
    ):
        self._color(self.arguments.cursor, foreground_color, background_color)
        return self

    def cursor_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.cursor,
            bold,
            italic,
            faint,
            underline,
            strikethrough,
        )
        return self

    def cursor_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        self._border(
            self.arguments.cursor, style, foreground_color, background_color
        )
        return self

    def cursor_size(self, width: int = None, height: int = None):
        self._size(self.arguments.cursor, width, height)
        return self

    def prompt(self, prompt: str):
        self._add_to_flag_set(self.arguments.prompt.prompt, prompt)
        return self

    def prompt_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.prompt, alignment, margin, padding)
        return self

    def prompt_color(
        self, foreground_color: str, background_color: str = None
    ):
        self._color(self.arguments.prompt, foreground_color, background_color)
        return self

    def prompt_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.prompt,
            bold,
            italic,
            faint,
            underline,
            strikethrough,
        )
        return self

    def prompt_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        self._border(
            self.arguments.prompt, style, foreground_color, background_color
        )
        return self

    def prompt_size(self, width: int = None, height: int = None):
        self._size(self.arguments.prompt, width, height)
        return self
