from typing import List

from gumpython.arguments import ChooseArgument
from gumpython.exceptions import ChooseArgumentError
from gumpython.style import GumStyle

from .command import GumCommand


class Choose(GumCommand):
    def __init__(self, item_list: List[str]):
        super().__init__()
        self.argument = "choose"
        self.returning = True
        self.item_list = item_list
        self._validate_item_list()
        self.arguments = ChooseArgument()

    def _validate_item_list(self):
        if not isinstance(self.item_list, list):
            raise ChooseArgumentError(
                f"'list' expected for item list argument but '{type(self.item_list).__name__}' is given."
            )
        for item in self.item_list:
            if not isinstance(item, str):
                raise ChooseArgumentError(f"{item} is not a string value.")
        return True

    def _compile_command(self):
        super(Choose, self)._compile_command()
        self.command.extend(self.item_list)

    def run(self):
        response = super(Choose, self).run()
        return response.split("\n")[:-1]

    def cursor(self, cursor_text: str):
        self._add_to_flag_set(self.arguments.cursor.cursor, cursor_text)
        return self

    def cursor_prefix(self, prefix: str):
        self._add_to_flag_set(self.arguments.cursor.prefix, prefix)
        return self

    def cursor_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.cursor)
        return self

    def items_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.item)
        return self

    def selected_prefix(self, prefix: str):
        self._add_to_flag_set(self.arguments.selected.prefix, prefix)
        return self

    def selected_style(self, style: GumStyle):
        self._compile_style(style, self.arguments.selected)
        return self

    def list_height(self, height: int):
        self._add_to_flag_set(self.arguments.list.height, height)
        return self

    def limit(self, limit: int):
        self._add_to_flag_set(self.arguments.list.limit, limit)
        return self

    def no_limit(self):
        self._add_to_flag_set(self.arguments.list.no_limit, True)
        return self

    def unselected_prefix(self, prefix: str):
        self._add_to_flag_set(self.arguments.list.unselected_prefix, prefix)
        return self
