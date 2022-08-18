from typing import List, Union

from gumpython.arguments import StyleArgument
from gumpython.exceptions import StyleArgumentError

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
            self.command.append(f"'{self.text}'")
        if isinstance(self.text, list):
            self.command.extend(list(map(lambda x: f"'{x}'", self.text)))

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
        self._border(
            self.arguments.border, style, foreground_color, background_color
        )
        return self

    def align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.text, alignment, margin, padding)
        return self

    def text_color(self, foreground, background=None):
        self._color(self.arguments.text, foreground, background)
        return self

    def text_font(
        self,
        bold: bool = False,
        faint: bool = False,
        italic: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.text, bold, faint, italic, underline, strikethrough
        )
        return self

    def size(self, width: int, height: int = None):
        self._size(self.arguments.text, width, height)
        return self
