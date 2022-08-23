from typing import List

from gumpython.arguments import FilterArguments
from gumpython.exceptions import FilterArgumentError
from gumpython.style import GumStyle

from .command import GumCommand


class Filter(GumCommand):
    """
    Filter items from a list
    """

    def __init__(self, item_list: List[str]):
        """
        Filter items from a list

        :param item_list: A list of strings that will be filtered
        :type item_list: List[str]
        """
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
        """
        Character for selection

        Example: "•" or "x" etc

        :param indicator: The indicator character
        :type indicator: str
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.indicator.indicator, indicator)
        return self

    def indicator_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the indicator.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.indicator)
        return self

    def match_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the matched results.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.match)
        return self

    def prompt(self, prompt: str):
        """
        The prompt to display

        Example: "> " or "-> " etc

        :param prompt: The prompt to display
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

    def text_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the text.

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """

        self._compile_style(style, self.arguments.text)
        return self

    def placeholder(self, placeholder: str):
        """
        Placeholder value

        :param placeholder: The placeholder text to display in the input field
        :type placeholder: str
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.general.placeholder, placeholder)
        return self

    def input_size(self, width: int = None, height: int = None):
        """
        This function takes in a width and height and sets the size of the input.

        :param width of the input (default None)
        :type width: int
        :param height of the input (default None)
        :type height: int
        :return: The object itself.
        """
        self._size(self.arguments.general, width, height)
        return self
