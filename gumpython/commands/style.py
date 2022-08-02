from typing import List, Union

from gumpython.arguments import StyleArgument
from gumpython.exceptions import StyleArgumentError
from gumpython.utils import (
    get_alignment_object,
    get_border_object,
    get_color_object,
    get_integer_input_object,
    get_position_object,
)

from .command import GumCommand


class Style(GumCommand):
    def __init__(self, text: Union[str, List[str]]):
        super().__init__()
        self.argument = "style"
        self.text = text
        self._validate_text_argument()
        self.arguments = StyleArgument()

    def _compile_command(self):
        super(Style, self)._compile_command()
        if isinstance(self.text, str):
            self.command.append(self.text)
        if isinstance(self.text, list):
            self.command.extend(self.text)

    def _validate_text_argument(self):
        if isinstance(self.text, str):
            return True
        if isinstance(self.text, list):
            for t in self.text:
                if not isinstance(t, str):
                    raise StyleArgumentError(f"{t} is not a string.")
            return True
        raise StyleArgumentError(
            f"Expected 'str' or List[str] but '{type(self.text).__name__}' is given."
        )

    def border(
        self,
        style: str = None,
        foreground_color: Union[str, tuple] = None,
        background_color: Union[str, tuple] = None,
    ):
        border = self.arguments.border
        if style:
            self._add_to_flag_set(border.style, get_border_object(style))
        if foreground_color:
            self._add_to_flag_set(
                border.foreground_color, get_color_object(foreground_color)
            )
        if background_color:
            self._add_to_flag_set(
                border.background_color, get_color_object(background_color)
            )
        return self

    def align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        text = self.arguments.text
        self._add_to_flag_set(
            text.align,
            get_alignment_object(alignment, text.align.display_name),
        )
        if margin:
            self._add_to_flag_set(
                text.margin,
                get_position_object(margin, text.margin.display_name),
            )
        if padding:
            self._add_to_flag_set(
                text.padding,
                get_position_object(padding, text.padding.display_name),
            )
        return self

    def text_color(self, foreground, background=None):
        self._add_to_flag_set(
            self.arguments.text.foreground_color, get_color_object(foreground)
        )
        if background:
            self._add_to_flag_set(
                self.arguments.text.background_color,
                get_color_object(background),
            )
        return self

    def text_font(
        self,
        bold: bool = False,
        faint: bool = False,
        italic: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        text_arg = self.arguments.text
        if bold:
            self._add_to_flag_set(text_arg.bold, None)
        if faint:
            self._add_to_flag_set(text_arg.faint, None)
        if italic:
            self._add_to_flag_set(text_arg.italic, None)
        if underline:
            self._add_to_flag_set(text_arg.underline, None)
        if strikethrough:
            self._add_to_flag_set(text_arg.strikethrough, None)
        return self

    def size(self, width: int, height: int = None):
        text_arg = self.arguments.text
        self._add_to_flag_set(
            text_arg.width,
            get_integer_input_object(width, text_arg.width.display_name),
        )
        if height:
            self._add_to_flag_set(
                text_arg.height,
                get_integer_input_object(height, text_arg.height.display_name),
            )
        return self
