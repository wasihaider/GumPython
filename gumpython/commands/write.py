from gumpython.arguments import WriteArguments
from gumpython.style import GumStyle

from .command import GumCommand


class Write(GumCommand):
    """
    Prompt for long-form text
    """

    def __init__(self):
        """
        Prompt for long-form text
        """
        super(Write, self).__init__()
        self.argument = "write"
        self.returning = True
        self.arguments = WriteArguments()

    def run(self):
        """
        Compiles and run the command.
        :return: A list of strings
        """
        response = super(Write, self).run()
        return list(filter(lambda x: x != "", response.split("\n")))

    def base_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the write field base.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.base)
        return self

    def cursor_line_number_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the cursor line numbers.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.cursor_line_number)
        return self

    def cursor_line_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the cursor line.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.cursor_line)
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

    def end_of_buffer_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the end of buffer.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.end_of_buffer)
        return self

    def line_number_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the line numbers.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.line_number)
        return self

    def placeholder(self, placeholder: str):
        """
        Set the placeholder in the input field

        :param placeholder: The placeholder text to display in the input field
        :type placeholder: str
        :return: The object itself.
        """
        self._add_to_flag_set(
            self.arguments.placeholder.placeholder, placeholder
        )
        return self

    def placeholder_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the placeholder.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.placeholder)
        return self

    def prompt(self, prompt: str):
        """
        Prompt to display

        Example: "| " or "~ " etc

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
        return self

    def char_limit(self, char_limit: int):
        """
        Maximum value length (0 for no limit)

        :param char_limit: The maximum number of characters in the input field
        :type char_limit: int
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.general.char_limit, char_limit)
        return self

    def height(self, height: int):
        """
        Set the height of input field

        :param height: The height of the input field
        :type height: int
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.general.height, height)
        return self

    def show_cursor_line(self):
        """
        Show cursor lines
        :return: self
        """
        self._add_to_flag_set(self.arguments.general.show_cursor_line, True)
        return self

    def show_line_numbers(self):
        """
        Show line numbers.
        :return:
        """
        self._add_to_flag_set(self.arguments.general.show_line_numbers, True)
        return self

    def value(self, value: str):
        """
        Set initial value in to input field

        :param value: The value to add to the input field
        :type value: str
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.general.value, value)
        return self

    def width(self, width: int):
        """
        Set width for the input field

        :param width: The width of the input field
        :type width: int
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.general.width, width)
        return self
