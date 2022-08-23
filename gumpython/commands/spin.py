import subprocess

from gumpython.arguments import SpinArguments
from gumpython.style import GumStyle

from .command import GumCommand


class Spin(GumCommand):
    """
    Display spinner while running a command
    """

    def __init__(self, exec_command: str, show_output=False):
        """
        Display spinner while running a command

        :param exec_command: The command to execute
        :type exec_command: str
        :param show_output: If True, the output of the command will be shown in the terminal, defaults to False (optional)
        """
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
        """
        Set the type of spinner.

        :param spinner_type: The type of spinner to use
        :type spinner_type: str
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.spinner.spinner, spinner_type)
        return self

    def spinner_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the spinner.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.spinner)
        return self

    def title(self, text: str):
        """
        Text to display to user while spinning.

        Example: "Loading..." or "Command is running in the background..." etc

        :param text: The text to be displayed in the title
        :type text: str
        :return: self
        """
        self._add_to_flag_set(self.arguments.title.title, f"'{text}'")
        return self

    def title_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the title.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.title)
        return self
