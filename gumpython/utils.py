from gumpython.exceptions import ColorInputError
from gumpython.inputs import (
    Border,
    Color
)


def get_color_object(value):
    if isinstance(value, str):
        return Color(hex_code=value)
    if isinstance(value, tuple):
        return Color(rgb=value)
    raise ColorInputError(f"Expected 'str' or 'tuple' input for color but '{type(value).__name__}' given.")


def get_border_object(border_type):
    return Border(border_type)
