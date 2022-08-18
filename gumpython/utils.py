from gumpython.exceptions import ColorInputError
from gumpython.inputs import (
    Alignment,
    Border,
    Color,
    Format,
    IntegerInput,
    Position,
    Spinner,
    StringInput,
)

from .constants import FlagTypeChoice


def get_color_object(value, flag_name):
    if isinstance(value, str):
        return Color(hex_code=value, flag_name=flag_name)
    if isinstance(value, tuple):
        return Color.from_rgb(value, flag_name=flag_name)
    raise ColorInputError(
        f"Expected 'str' or 'tuple' input for color but '{type(value).__name__}' given."
    )


def get_border_object(border_type, flag_name):
    return Border(border_type, flag_name)


def get_string_input_object(value, flag_name):
    return StringInput(value, flag_name)


def get_integer_input_object(value, flag_name):
    return IntegerInput(value, flag_name)


def get_alignment_object(value, flag_name):
    return Alignment(value, flag_name)


def get_position_object(value, flag_name):
    return Position(value, flag_name)


def get_format_object(value, flag_name):
    return Format(value, flag_name)


def get_spinner_object(value, flag_name):
    return Spinner(value, flag_name)


FLAG_TYPE_INPUT_MAPPING = {
    FlagTypeChoice.COLOR: get_color_object,
    FlagTypeChoice.INT: get_integer_input_object,
    FlagTypeChoice.STR: get_string_input_object,
    FlagTypeChoice.ALIGN: get_alignment_object,
    FlagTypeChoice.POSITION: get_position_object,
    FlagTypeChoice.BORDER: get_border_object,
    FlagTypeChoice.FORMAT: get_format_object,
    FlagTypeChoice.SPINNER: get_spinner_object,
}


def get_input_object(flag_type, value, flag_name):
    func = FLAG_TYPE_INPUT_MAPPING.get(flag_type)
    return func(value, flag_name)
