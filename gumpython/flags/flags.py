from dataclasses import dataclass

from gumpython.inputs import Input


@dataclass
class Flag:
    name: str
    type: str
    _value: Input = None
    _display_name: str = None

    @property
    def flag(self):
        return f"--{self.name}"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Input):
        if value.is_valid():
            self._value = value

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
