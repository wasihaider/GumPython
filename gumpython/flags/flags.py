from dataclasses import dataclass
from gumpython.inputs import Input
from gumpython.constants import FlagTypeChoice, FlagSeparatorChoice


@dataclass
class Flag:
    name: str
    type: str
    _value: Input = None

    @property
    def flag(self):
        return f"--{self.name}"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Input):
        if value.is_valid():
            print(f"The value is valid for {self.name}")
            self._value = value

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

    def __hash__(self):
        return hash((self.name, self.sub_name))
