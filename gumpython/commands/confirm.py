from gumpython.arguments import ConfirmArguments
from gumpython.exceptions import ConfirmArgumentError
from gumpython.run_command import run_command
from gumpython.style import GumStyle

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

    def prompt_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.prompt)
        return self

    def selected_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.selected)
        return self

    def unselected_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.unselected)
        return self
