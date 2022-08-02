from gumpython.exceptions import PositionInputError

from .inputs import Input


class Position(Input):
    def __init__(self, value: tuple, flag_name: str):
        self.value = value
        self.flag_name = flag_name

    def is_valid(self):
        return self._validate()

    def _validate(self):
        if not isinstance(self.value, tuple):
            raise PositionInputError(
                f"'tuple' is expected for {self.flag_name} but '{type(self.value).__name__}' is given."
            )
        if len(self.value) != 2:
            raise PositionInputError(
                f"'(x, y)' expected for {self.flag_name} but '{self.value}' is given."
            )
        if not isinstance(self.value[0], int) or not isinstance(
            self.value[1], int
        ):
            raise PositionInputError(
                f"'int' values expected for {self.flag_name}."
            )
        return True

    def compile(self):
        return f"{self.value[0]} {self.value[1]}"
