from gumpython.exceptions import SpinnerInputError

from .help_inputs.spinner_types import get_all_spinner_types
from .inputs import Input


class Spinner(Input):
    def __init__(self, spinner_type, flag_name):
        self.spinner_type = spinner_type
        self.flag_name = flag_name

    def is_valid(self):
        return self._validate()

    def _validate(self):
        if not isinstance(self.spinner_type, str):
            raise SpinnerInputError(
                f"'str' input expected for {self.flag_name} format type but '{type(self.spinner_type).__name__}' is given"
            )
        if self.spinner_type not in get_all_spinner_types():
            raise SpinnerInputError(
                f"border must be one of {get_all_spinner_types()} but got '{self.spinner_type}'"
            )
        return True

    def compile(self):
        return self.spinner_type
