from gumpython.exceptions import ColorInputError
from gumpython.inputs import (
    Alignment,
    Border,
    Color,
    IntegerInput,
    Position,
    StringInput,
)


def get_color_object(value):
    if isinstance(value, str):
        return Color(hex_code=value)
    if isinstance(value, tuple):
        return Color.from_rgb(value)
    raise ColorInputError(
        f"Expected 'str' or 'tuple' input for color but '{type(value).__name__}' given."
    )


def get_border_object(border_type):
    return Border(border_type)


def get_string_input_object(value, flag_name):
    return StringInput(value, flag_name)


def get_integer_input_object(value, flag_name):
    return IntegerInput(value, flag_name)


def get_alignment_object(value, flag_name):
    return Alignment(value, flag_name)


def get_position_object(value, flag_name):
    return Position(value, flag_name)
