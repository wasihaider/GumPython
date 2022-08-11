from dataclasses import dataclass

from gumpython.utils import get_input_object


@dataclass
class Flag:
    name: str
    type: str
    _value = None
    _display_name: str = None

    @property
    def flag(self):
        return f"--{self.name}"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        input_obj = get_input_object(self.type, value, self.display_name)
        if input_obj.is_valid():
            self._value = input_obj

    @property
    def display_name(self):
        return self.name

    def get_command(self):
        return f"{self.flag}={self.value.compile()}"

    def __hash__(self):
        return hash((self.name,))


@dataclass
class SubFlag(Flag):
    sub_name: str = None
    separator: str = None

    @property
    def flag(self):
        return f"--{self.name}{self.separator}{self.sub_name}"

    @property
    def display_name(self):
        return f"{self.name} {self.sub_name}"

    def __hash__(self):
        return hash((self.name, self.sub_name))
