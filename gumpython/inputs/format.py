from gumpython.exceptions import FormatInputError

from .help_inputs.format_types import all_format_types
from .inputs import Input


class Format(Input):
    def __init__(self, format_type, flag_name):
        self.format_type = format_type
        self.flag_name = flag_name

    def is_valid(self):
        return self._validate()

    def _validate(self):
        if not isinstance(self.format_type, str):
            raise FormatInputError(
                f"'str' input expected for {self.flag_name} format type but '{type(self.format_type).__name__}' is given"
            )
        if self.format_type not in all_format_types():
            raise FormatInputError(
                f"border must be one of {all_format_types()} but got '{self.format_type}'"
            )
        return True

    def compile(self):
        return self.format_type
