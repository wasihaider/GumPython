from gumpython.arguments import ConfirmArguments
from gumpython.exceptions import ConfirmArgumentError
from gumpython.run_command import run_command
from gumpython.style import GumStyle

from .command import GumCommand


class Confirm(GumCommand):
    """
    Ask a user to confirm an action
    """

    def __init__(self, message: str):
        """
        Ask a user to confirm an action

        :param message: The message to display to the user
        :type message: str
        """
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
        """
        It compiles the command, runs it, and returns whether it succeeded or not
        :return: Boolean.
        """
        self._compile_command()
        response = run_command(self.command, self.input)
        return response.returncode == 0

    def affirmative(self, text: str):
        """
        The title of the affirmative action

        Example: "Yes" or "Delete" etc

        :param text: The text to add to the affirmative action button
        :type text: str
        :return: self
        """
        self._add_to_flag_set(self.arguments.general.affirmative, text)
        return self

    def negative(self, text: str):
        """
        The title of the negative action

        Example: "No" or "Restore" etc

        :param text: The text to add to the negative button
        :type text: str
        :return: self
        """
        self._add_to_flag_set(self.arguments.general.negative, text)
        return self

    def prompt_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the prompt.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.prompt)
        return self

    def selected_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the selected action.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.selected)
        return self

    def unselected_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the unselected action.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.unselected)
        return self
