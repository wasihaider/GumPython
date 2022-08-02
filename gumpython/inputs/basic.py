from gumpython.exceptions import InputError

from .inputs import Input


class IntegerInput(Input):
    def __init__(self, value: int, flag_name):
        self.value = value
        self.flag_name = flag_name

    def is_valid(self):
        return self._validate()

    def _validate(self):
        if isinstance(self.value, int):
            return True
        raise InputError(
            f"'int' input expected for {self.flag_name} but given '{type(self.value).__name__}'"
        )

    def compile(self):
        return self.value


class StringInput(Input):
    def __init__(self, value: str, flag_name):
        self.value = value
        self.flag_name = flag_name

    def is_valid(self):
        return self._validate()

    def _validate(self):
        if isinstance(self.value, str):
            return True
        raise InputError(
            f"'str' input expected for {self.flag_name} but given '{type(self.value).__name__}'"
        )

    def compile(self):
        return self.value
