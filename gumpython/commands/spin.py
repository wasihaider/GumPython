import subprocess

from gumpython.arguments import SpinArguments
from gumpython.style import GumStyle

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

    def spinner_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.spinner)
        return self

    def title(self, text: str):
        self._add_to_flag_set(self.arguments.title.title, f"'{text}'")
        return self

    def title_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.title)
        return self
