from typing import List

from gumpython.arguments import ChooseArgument
from gumpython.exceptions import ChooseArgumentError
from gumpython.utils import (
    get_alignment_object,
    get_border_object,
    get_color_object,
    get_integer_input_object,
    get_position_object,
    get_string_input_object,
)

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
        self._add_to_flag_set(
            cursor_arg.cursor,
            get_string_input_object(
                cursor_text, cursor_arg.cursor.display_name
            ),
        )
        if prefix:
            self._add_to_flag_set(
                cursor_arg.prefix,
                get_string_input_object(
                    prefix, cursor_arg.prefix.display_name
                ),
            )
        return self

    def cursor_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        cursor = self.arguments.cursor
        self._add_to_flag_set(
            cursor.align,
            get_alignment_object(alignment, cursor.align.display_name),
        )
        if margin:
            self._add_to_flag_set(
                cursor.margin,
                get_position_object(margin, cursor.margin.display_name),
            )
        if padding:
            self._add_to_flag_set(
                cursor.padding,
                get_position_object(padding, cursor.padding.display_name),
            )
        return self

    def cursor_color(
        self, foreground_color: str, background_color: str = None
    ):
        cursor = self.arguments.cursor
        self._add_to_flag_set(
            cursor.foreground, get_color_object(foreground_color)
        )
        if background_color:
            self._add_to_flag_set(
                cursor.background, get_color_object(background_color)
            )
        return self

    def cursor_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        cursor = self.arguments.cursor
        if bold:
            self._add_to_flag_set(cursor.bold, None)
        if italic:
            self._add_to_flag_set(cursor.italic, None)
        if faint:
            self._add_to_flag_set(cursor.faint, None)
        if underline:
            self._add_to_flag_set(cursor.underline, None)
        if strikethrough:
            self._add_to_flag_set(cursor.strikethrough, None)
        return self

    def cursor_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        cursor = self.arguments.cursor
        self._add_to_flag_set(cursor.border, get_border_object(style))
        if foreground_color:
            self._add_to_flag_set(
                cursor.border_foreground, get_color_object(foreground_color)
            )
        if background_color:
            self._add_to_flag_set(
                cursor.border_background, get_color_object(background_color)
            )
        return self

    def size(self, width: int = None, height: int = None):
        cursor = self.arguments.cursor
        if width:
            self._add_to_flag_set(
                cursor.width,
                get_integer_input_object(width, cursor.width.display_name),
            )
        if height:
            self._add_to_flag_set(
                cursor.height,
                get_integer_input_object(height, cursor.height.display_name),
            )
        return self
