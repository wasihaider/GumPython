import subprocess

from gumpython.arguments import SpinArguments

from .command import GumCommand


class Spin(GumCommand):
    def __init__(self, exec_command: str, show_output=False):
        super(Spin, self).__init__()
        self.argument = "spin"
        self.exec_command = exec_command
        self.show_output = show_output
        self.arguments = SpinArguments()

    def _compile_command(self):
        if self.show_output:
            self._add_to_flag_set(self.arguments.general.show_output, True)
        super(Spin, self)._compile_command()
        self.command.append(self.exec_command)

    def run(self):
        subprocess.run(self.get_command(), shell=True)

    def spinner(self, spinner_type: str):
        self._add_to_flag_set(self.arguments.spinner.spinner, spinner_type)
        return self

    def spinner_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.spinner, alignment, margin, padding)
        return self

    def spinner_color(
        self, foreground_color: str, background_color: str = None
    ):
        self._color(self.arguments.spinner, foreground_color, background_color)
        return self

    def spinner_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.spinner,
            bold,
            italic,
            faint,
            underline,
            strikethrough,
        )
        return self

    def spinner_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        self._border(
            self.arguments.spinner, style, foreground_color, background_color
        )
        return self

    def spinner_size(self, width: int = None, height: int = None):
        self._size(self.arguments.spinner, width, height)
        return self

    def title(self, text: str):
        self._add_to_flag_set(self.arguments.title.title, f"'{text}'")
        return self

    def title_align(
        self, alignment: str, margin: tuple = None, padding: tuple = None
    ):
        self._align(self.arguments.title, alignment, margin, padding)
        return self

    def title_color(self, foreground_color: str, background_color: str = None):
        self._color(self.arguments.title, foreground_color, background_color)
        return self

    def title_style(
        self,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        self._font_style(
            self.arguments.title,
            bold,
            italic,
            faint,
            underline,
            strikethrough,
        )
        return self

    def title_border(
        self,
        style: str,
        foreground_color: str = None,
        background_color: str = None,
    ):
        self._border(
            self.arguments.title, style, foreground_color, background_color
        )
        return self

    def title_size(self, width: int = None, height: int = None):
        self._size(self.arguments.title, width, height)
        return self
