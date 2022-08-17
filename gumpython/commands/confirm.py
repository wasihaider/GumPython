from gumpython.arguments import ConfirmArguments
from gumpython.exceptions import ConfirmArgumentError
from gumpython.run_command import run_command

from .command import GumCommand


class Confirm(GumCommand):
    def __init__(self, message: str):
        super(Confirm, self).__init__()
        self.argument = "confirm"
        self.message = message
        self._validate_message()
        self.arguments = ConfirmArguments()
        self.returning = True

    def _compile_command(self):
        super(Confirm, self)._compile_command()
        self.command.append(self.message)

    def _validate_message(self):
        if not isinstance(self.message, str):
            raise ConfirmArgumentError(
                f"'str' expected for message argument but '{type(self.message).__name__}' is given."
            )

    def run(self):
        self._compile_command()
        response = run_command(self.command, self.input)
        return response.returncode == 0

    def affirmative(self, text: str):
        self._add_to_flag_set(self.arguments.general.affirmative, text)
        return self

    def negative(self, text: str):
        self._add_to_flag_set(self.arguments.general.negative, text)
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

    def unselected_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.unselected, alignment, margin, padding)
        return self

    def unselected_color(
        self, foreground_color: str, background_color: str = None
    ):
        self._color(
            self.arguments.unselected, foreground_color, background_color
        )
        return self

    def unselected_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.unselected,
            bold,
            italic,
            faint,
            underline,
            strikethrough,
        )
        return self

    def unselected_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        self._border(
            self.arguments.unselected,
            style,
            foreground_color,
            background_color,
        )
        return self

    def unselected_size(self, width: int = None, height: int = None):
        self._size(self.arguments.unselected, width, height)
        return self
