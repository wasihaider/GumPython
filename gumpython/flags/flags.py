from abc import abstractmethod
from dataclasses import dataclass

from gumpython.constants import FlagSeparatorChoice, FlagTypeChoice
from gumpython.inputs import Input
from gumpython.utils import get_input_object


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


class BaseFlag:
    def __init__(self):
        self.flag_name = self.get_flag_name()

        # align
        self.align = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.ALIGN,
            sub_name="align",
            separator=FlagSeparatorChoice.DOT,
        )
        self.margin = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.POSITION,
            sub_name="margin",
            separator=FlagSeparatorChoice.DOT,
        )
        self.padding = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.POSITION,
            sub_name="padding",
            separator=FlagSeparatorChoice.DOT,
        )

        # color
        self.background = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.COLOR,
            sub_name="background",
            separator=FlagSeparatorChoice.DOT,
        )
        self.foreground = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.COLOR,
            sub_name="foreground",
            separator=FlagSeparatorChoice.DOT,
        )

        # style
        self.bold = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.BOOL,
            sub_name="bold",
            separator=FlagSeparatorChoice.DOT,
        )
        self.faint = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.BOOL,
            sub_name="faint",
            separator=FlagSeparatorChoice.DOT,
        )
        self.italic = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.BOOL,
            sub_name="italic",
            separator=FlagSeparatorChoice.DOT,
        )
        self.strikethrough = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.BOOL,
            sub_name="strikethrough",
            separator=FlagSeparatorChoice.DOT,
        )
        self.underline = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.BOOL,
            sub_name="underline",
            separator=FlagSeparatorChoice.DOT,
        )

        # border
        self.border = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.BORDER,
            sub_name="border",
            separator=FlagSeparatorChoice.DOT,
        )
        self.border_background = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.COLOR,
            sub_name="border-background",
            separator=FlagSeparatorChoice.DOT,
        )
        self.border_foreground = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.COLOR,
            sub_name="border-foreground",
            separator=FlagSeparatorChoice.DOT,
        )

        # size
        self.height = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.INT,
            sub_name="height",
            separator=FlagSeparatorChoice.DOT,
        )
        self.width = SubFlag(
            name=self.flag_name,
            type=FlagTypeChoice.INT,
            sub_name="width",
            separator=FlagSeparatorChoice.DOT,
        )

    @abstractmethod
    def get_flag_name(self):
        return ""
