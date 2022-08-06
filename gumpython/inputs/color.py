import re

from gumpython.exceptions import ColorInputError

from .inputs import Input


def is_valid_rgb(rgb: tuple):
    if not isinstance(rgb, tuple):
        raise ColorInputError(
            f"rgb should be of type 'tuple' but '{type(rgb).__name__}' given."
        )
    if len(rgb) != 3:
        raise ColorInputError(f"Expected (r, g, b) but given {rgb}")
    if rgb:
        for code in rgb:
            if code < 0 or code > 255:
                raise ColorInputError(f"{rgb} is not a valid rgb color code.")
        return True


def convert_rgb_to_hex(rgb: tuple):
    """
    It takes a tuple of three integers, representing the red, green, and blue values of a color, and returns a string
    containing the hexadecimal representation of that color

    :param rgb: tuple
    :type rgb: tuple
    :return: A string in the format of a hexadecimal color code.
    """
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"


class Color(Input):
    def __init__(self, hex_code: str = None):
        self.hex = hex_code

    @classmethod
    def from_rgb(cls, rgb: tuple):
        if is_valid_rgb(rgb):
            return cls(convert_rgb_to_hex(rgb))

    def is_valid(self):
        return self._validate()

    def _validate(self):
        if not isinstance(self.hex, str):
            raise ColorInputError(
                f"Hex should be a string but '{type(self.hex).__name__}' given."
            )
        regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
        p = re.compile(regex)
        if re.search(p, self.hex):
            return True
        else:
            raise ColorInputError(f"{self.hex} is not a valid hex color code")

    def compile(self):
        if self.hex:
            return self.hex
        if self.rgb:
            return self._convert_rgb_to_hex()
