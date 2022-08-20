from gumpython.arguments import WriteArguments
from gumpython.style import GumStyle

from .command import GumCommand


class Write(GumCommand):
    def __init__(self):
        super(Write, self).__init__()
        self.argument = "write"
        self.returning = True
        self.arguments = WriteArguments()

    def run(self):
        response = super(Write, self).run()
        return list(filter(lambda x: x != "", response.split("\n")))

    def base_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.base)
        return self

    def cursor_line_number_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.cursor_line_number)
        return self

    def cursor_line_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.cursor_line)
        return self

    def cursor_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.cursor)
        return self

    def end_of_buffer_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.end_of_buffer)
        return self

    def line_number_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.line_number)
        return self

    def placeholder(self, placeholder: str):
        self._add_to_flag_set(
            self.arguments.placeholder.placeholder, placeholder
        )
        return self

    def placeholder_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.placeholder)
        return self

    def prompt(self, prompt: str):
        self._add_to_flag_set(self.arguments.prompt.prompt, prompt)
        return self

    def prompt_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.prompt)
        return self

    def char_limit(self, char_limit: int):
        self._add_to_flag_set(self.arguments.general.char_limit, char_limit)
        return self

    def height(self, height: int):
        self._add_to_flag_set(self.arguments.general.height, height)
        return self

    def show_cursor_line(self):
        self._add_to_flag_set(self.arguments.general.show_cursor_line, True)
        return self

    def show_line_numbers(self):
        self._add_to_flag_set(self.arguments.general.show_line_numbers, True)
        return self

    def value(self, value: str):
        self._add_to_flag_set(self.arguments.general.value, value)
        return self

    def width(self, width: int):
        self._add_to_flag_set(self.arguments.general.width, width)
        return self
