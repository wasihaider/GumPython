from typing import List

from gumpython.arguments import ChooseArgument
from gumpython.exceptions import ChooseArgumentError
from gumpython.style import GumStyle

from .command import GumCommand


# It's a command that chooses a random item from a list of items
class Choose(GumCommand):
    """
    Choose an option from a list of choices.

    The default limit to select items is 1. If you want to update this then use limit or no_limit methods.
    :type item_list: List[str]
    """

    def __init__(self, item_list: List[str]):
        """
        Choose an option from a list of choices.

        The default limit to select items is 1. If you want to update this then use limit or no_limit methods.

        :param item_list: A list of strings that will be the options for the user to choose from
        :type item_list: List[str]
        """
        super().__init__()
        self.argument = "choose"
        self.returning = True
        self.item_list = item_list
        self._validate_item_list()
        self.arguments = ChooseArgument()

    def _validate_item_list(self):
        """
        It checks if the item list is a list and if each item in the list is a string
        :return: a boolean value.
        """
        if not isinstance(self.item_list, list):
            raise ChooseArgumentError(
                f"'list' expected for item list argument but '{type(self.item_list).__name__}' is given."
            )
        for item in self.item_list:
            if not isinstance(item, str):
                raise ChooseArgumentError(f"{item} is not a string value.")
        return True

    def _compile_command(self):
        """
        It takes the command that was passed to the constructor and adds the list of items to it
        """
        super(Choose, self)._compile_command()
        self.command.extend(self.item_list)

    def run(self):
        """
        Run the choose command.
        :return: A list of strings
        """
        response = super(Choose, self).run()
        return response.split("\n")[:-1]

    def cursor(self, cursor_text: str):
        """
        This function adds a cursor. A cursor here is a prefix to show on item that corresponds to the cursor position.

        Example: "> " or "* " etc

        :param cursor_text: The text to be displayed as the cursor
        :type cursor_text: str
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.cursor.cursor, cursor_text)
        return self

    def cursor_prefix(self, prefix: str):
        """
        Adds a prefix to the cursor.

        Prefix to show on the cursor item (hidden if limit is 1)
        Example: "[.] " or "[*] " etc

        :param prefix: The prefix to use for the cursor
        :type prefix: str
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.cursor.prefix, prefix)
        return self

    def cursor_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the cursor

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.cursor)
        return self

    def items_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the items in the list

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.item)
        return self

    def selected_prefix(self, prefix: str):
        """
        Prefix to show on selected items (hidden if limit is 1)

        Example: "[x] " or "[selected] " etc

        :param prefix: The prefix to add to the selected prefix set
        :type prefix: str
        :return: self
        """
        self._add_to_flag_set(self.arguments.selected.prefix, prefix)
        return self

    def selected_style(self, style: GumStyle):
        """
        This method compiles the GumStyle object given and applies it to the selected item

        :param style: The style to compile
        :type style: GumStyle
        :return: The object itself.
        """
        self._compile_style(style, self.arguments.selected)
        return self

    def list_height(self, height: int):
        """
        Set the height of the list

        :param height: The height of the list
        :type height: int
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.list.height, height)
        return self

    def limit(self, limit: int):
        """
        Maximum number of options to pick (default is 1)

        :param limit: The maximum number of items to select
        :type limit: int
        :return: The object itself.
        """
        self._add_to_flag_set(self.arguments.list.limit, limit)
        return self

    def no_limit(self):
        """
        Pick unlimited number of options (ignores limit)
        :return: self
        """
        self._add_to_flag_set(self.arguments.list.no_limit, True)
        return self

    def unselected_prefix(self, prefix: str):
        """
        Prefix to show on unselected items (hidden if limit is 1)

        :param prefix: The prefix to add to the unselected items
        :type prefix: str
        :return: self
        """
        self._add_to_flag_set(self.arguments.list.unselected_prefix, prefix)
        return self
