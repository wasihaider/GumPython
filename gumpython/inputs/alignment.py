from gumpython.exceptions import AlignmentInputError

from .help_inputs.alignment_types import all_alignment_types
from .inputs import Input


class Alignment(Input):
    def __init__(self, alignment_type: str, flag_name: str):
        self.alignment_type = alignment_type
        self.flag_name = flag_name

    def is_valid(self):
        return self._validate()

    def _validate(self):
        if not isinstance(self.alignment_type, str):
            raise AlignmentInputError(
                f"'str' expected for {self.flag_name} but '{type(self.alignment_type).__name__}' is given."
            )
        if self.alignment_type not in all_alignment_types():
            raise AlignmentInputError(
                f"Alignment must be one of {all_alignment_types()} but '{self.alignment_type}' is given."
            )
        return True

    def compile(self):
        return self.alignment_type
