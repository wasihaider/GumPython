from typing import List

from gumpython.arguments import ChooseArgument
from gumpython.exceptions import ChooseArgumentError

from .command import GumCommand


class Choose(GumCommand):
    def __init__(self, item_list: List[str]):
        super().__init__()
        self.argument = "choose"
        self.item_list = item_list
        self._validate_item_list()
        self.arguments = ChooseArgument()

    def _validate_item_list(self):
        if not isinstance(self.item_list, list):
            raise ChooseArgumentError(
                f"'list' expected for item list argument but '{type(self.item_list).__name__}' is given."
            )
        for item in self.item_list:
            if not isinstance(item, str):
                raise ChooseArgumentError(f"{item} is not a string value.")
        return True

    def _compile_command(self):
        super(Choose, self)._compile_command()
        self.command.extend(self.item_list)

    def cursor(self, cursor_text: str, prefix: str = None):
        cursor_arg = self.arguments.cursor
        self._add_to_flag_set(cursor_arg.cursor, cursor_text)
        if prefix:
            self._add_to_flag_set(cursor_arg.prefix, prefix)
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
        self._size(self.arguments, width, height)
        return self
