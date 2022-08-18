import subprocess
from typing import List, Union

from gumpython.arguments import JoinArguments
from gumpython.exceptions import JoinArgumentError

from .command import GumCommand
from .style import Style


class Join(GumCommand):
    def __init__(self, items=List[Union[str, GumCommand]]):
        super(Join, self).__init__()
        self.argument = "join"
        self.items = items
        self.__parsed_items = []
        self._validate_and_parse_items()
        self.arguments = JoinArguments()
        self.__vertical = False

    def _validate_and_parse_items(self):
        if not self.items:
            raise JoinArgumentError("Items can not be empty.")
        if not isinstance(self.items, list):
            raise JoinArgumentError(
                f"'list' expected for items but '{type(self.items).__name__}' given."
            )
        for item in self.items:
            if isinstance(item, str):
                self.__parsed_items.append(item)
            elif isinstance(item, (Style, self.__class__)):
                self.__parsed_items.append(f'"$({item.get_command()})"')
            else:
                raise JoinArgumentError(
                    f"{item} is not of type 'str' or 'gumpython.Style'"
                )

    def _compile_command(self):
        self._add_to_flag_set(
            self.arguments.text.vertical
            if self.__vertical
            else self.arguments.text.horizontal,
            True,
        )
        super(Join, self)._compile_command()
        self.command.extend(self.__parsed_items)

    def run(self):
        subprocess.run(self.get_command(), shell=True)

    def align(self, alignment: str):
        self._add_to_flag_set(self.arguments.text.align, alignment)
        return self

    def vertical(self):
        self.__vertical = True
        return self
