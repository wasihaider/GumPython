from dataclasses import dataclass
from gumpython.validators import Validator


class FlagTypeChoice:
    COLOR = "color"
    INT = "integer"
    STR = "string"
    ALIGN = "alignment"


class FlagSeparatorChoice:
    DOT = "."
    HYPHEN = "-"


@dataclass
class FlagType:
    name: str
    validator: Validator = None

    def __post_init__(self):
        self.validator = Validator(self.name)


@dataclass
class Flag:
    name: str
    type: FlagType
    default: str = None
    _value: str = None

    def __post_init__(self):
        if self.default:
            self._value = self.default

    @property
    def flag(self):
        return f"--{self.name}"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get_command(self):
        if self.value:
            return [self.flag, self.value]
        return None


@dataclass
class SubFlag(Flag):
    sub_name: str = None
    separator: str = None

    @property
    def flag(self):
        return f"--{self.name}{self.separator}{self.sub_name}"
