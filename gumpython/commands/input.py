from gumpython.arguments import InputArguments
from gumpython.style import GumStyle

from .command import GumCommand


class Input(GumCommand):
    """
    Prompt for some input
    """

    def __init__(self):
        super(Input, self).__init__()
        self.argument = "input"
        self.arguments = InputArguments()
        self.returning = True

    def run(self):
        """
        Compiles and run the input.

        :return: Input given by user.
        """
        response = super(Input, self).run()
        return response[:-1]

    def char_limit(self, limit: int):
        """
        Maximum value length for input (0 for no limit)

        :param limit: The maximum number of characters in input
        :type limit: int
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.general.char_limit, limit)
        return self

    def password(self):
        """
        Hide the input character.
        :return: self
        """
        self._add_to_flag_set(self.arguments.general.password, True)
        return self

    def placeholder(self, placeholder: str):
        """
        Set a placeholder value for input field

        :param placeholder: The placeholder text to display in the input field
        :type placeholder: str
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.general.placeholder, placeholder)
        return self

    def value(self, value: str):
        """
        Initial value in the input field.

        :param value: The value to add input field
        :type value: str
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.general.value, value)
        return self

    def width(self, width: int):
        """
        Set the width for input field.

        :param width: The width of input field
        :type width: int
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.general.width, width)
        return self

    def cursor_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the cursor.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.cursor)
        return self

    def prompt(self, prompt: str):
        """
        Prompt to display

        Example: "> " or "-> " etc

        :param prompt: The prompt to display to the user
        :type prompt: str
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.prompt.prompt, prompt)
        return self

    def prompt_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the prompt.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.prompt)
