from typing import List

from gumpython.arguments import FilterArguments
from gumpython.exceptions import FilterArgumentError

from .command import GumCommand


class Filter(GumCommand):
    def __init__(self, item_list: List[str]):
        super(Filter, self).__init__()
        self.argument = "filter"
        self.item_list = item_list
        self._validate_item_list()
        self.input = "\n".join(self.item_list)
        self.arguments = FilterArguments()

    def _validate_item_list(self):
        if not isinstance(self.item_list, list):
            raise FilterArgumentError(
                f"'list' expected for item list argument but '{type(self.item_list).__name__}' is given."
            )
        if not self.item_list:
            raise FilterArgumentError("'item_list' can not be an empty list.")
        for item in self.item_list:
            if not isinstance(item, str):
                raise FilterArgumentError(f"{item} is not a string value.")
        return True

    def indicator(self, indicator: str):
        self._add_to_flag_set(self.arguments.indicator.indicator, indicator)
        return self

    def indicator_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.indicator, alignment, margin, padding)
        return self

    def indicator_color(
        self, foreground_color: str, background_color: str = None
    ):
        self._color(
            self.arguments.indicator, foreground_color, background_color
        )
        return self

    def indicator_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.indicator,
            bold,
            italic,
            faint,
            underline,
            strikethrough,
        )
        return self

    def indicator_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        self._border(
            self.arguments.indicator, style, foreground_color, background_color
        )
        return self

    def indicator_size(self, width: int = None, height: int = None):
        self._size(self.arguments.indicator, width, height)
        return self

    def match_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.match, alignment, margin, padding)
        return self

    def match_color(self, foreground_color: str, background_color: str = None):
        self._color(self.arguments.match, foreground_color, background_color)
        return self

    def match_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.match,
            bold,
            italic,
            faint,
            underline,
            strikethrough,
        )
        return self

    def match_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        self._border(
            self.arguments.match, style, foreground_color, background_color
        )
        return self

    def match_size(self, width: int = None, height: int = None):
        self._size(self.arguments.match, width, height)
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

    def text_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.text, alignment, margin, padding)
        return self

    def text_color(self, foreground_color: str, background_color: str = None):
        self._color(self.arguments.text, foreground_color, background_color)
        return self

    def text_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.text,
            bold,
            italic,
            faint,
            underline,
            strikethrough,
        )
        return self

    def text_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        self._border(
            self.arguments.text, style, foreground_color, background_color
        )
        return self

    def text_size(self, width: int = None, height: int = None):
        self._size(self.arguments.text, width, height)
        return self

    def placeholder(self, placeholder: str):
        self._add_to_flag_set(self.arguments.general.placeholder, placeholder)
        return self

    def input_size(self, width: int = None, height: int = None):
        self._size(self.arguments.general, width, height)
        return self
