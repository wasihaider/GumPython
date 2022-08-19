from gumpython.arguments import InputArguments
from gumpython.style import GumStyle

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

    def cursor_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.cursor)
        return self

    def prompt(self, prompt: str, style: GumStyle = None):
        self._add_to_flag_set(self.arguments.prompt.prompt, prompt)
        return self

    def prompt_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.prompt)
