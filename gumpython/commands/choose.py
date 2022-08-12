from typing import List

from gumpython.arguments import ChooseArgument
from gumpython.exceptions import ChooseArgumentError

from .command import GumCommand


class Choose(GumCommand):
    def __init__(self, item_list: List[str]):
        super().__init__()
        self.argument = "choose"
        self.returning = True
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

    def run(self):
        response = super(Choose, self).run()
        return response.split("\n")[:-1]

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
        self._size(self.arguments.cursor, width, height)
        return self

    def items_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.item, alignment, margin, padding)
        return self

    def items_color(self, foreground_color: str, background_color: str = None):
        self._color(self.arguments.item, foreground_color, background_color)
        return self

    def items_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.item,
            bold,
            italic,
            faint,
            underline,
            strikethrough,
        )
        return self

    def items_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        self._border(
            self.arguments.item, style, foreground_color, background_color
        )
        return self

    def items_size(self, width: int = None, height: int = None):
        self._size(self.arguments.item, width, height)
        return self

    def selected_prefix(self, prefix: str):
        self._add_to_flag_set(self.arguments.selected.prefix, prefix)
        return self

    def selected_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.selected, alignment, margin, padding)
        return self

    def selected_color(
        self, foreground_color: str, background_color: str = None
    ):
        self._color(
            self.arguments.selected, foreground_color, background_color
        )
        return self

    def selected_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.selected,
            bold,
            italic,
            faint,
            underline,
            strikethrough,
        )
        return self

    def selected_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        self._border(
            self.arguments.selected, style, foreground_color, background_color
        )
        return self

    def selected_size(self, width: int = None, height: int = None):
        self._size(self.arguments.selected, width, height)
        return self

    def list_height(self, height: int):
        self._add_to_flag_set(self.arguments.list.height, height)
        return self

    def limit(self, limit: int):
        self._add_to_flag_set(self.arguments.list.limit, limit)
        return self

    def no_limit(self):
        self._add_to_flag_set(self.arguments.list.no_limit, True)
        return self

    def unselected_prefix(self, prefix: str):
        self._add_to_flag_set(self.arguments.list.unselected_prefix, prefix)
        return self
