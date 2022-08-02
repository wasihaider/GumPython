import re
from .inputs import Input
from gumpython.exceptions import ColorInputError


class Color(Input):
    def __init__(self, hex: str = None, rgb: tuple = None):
        self.hex = hex
        self.rgb = rgb

    def is_valid(self):
        return self._validate()

    def _validate(self):
        if self.hex:
            return self._validate_hex()
        if self.rgb:
            return self._validate_rgb()
        raise ColorInputError("Expected hex or rgb value but None given.")

    def _validate_hex(self):
        if not isinstance(self.hex, str):
            raise ColorInputError(f"Hex should be a string but '{type(self.hex).__name__}' given.")
        regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
        p = re.compile(regex)
        if re.search(p, self.hex):
            return True
        else:
            raise ColorInputError(f"{self.hex} is not a valid hex color code")

    def _validate_rgb(self):
        if isinstance(self.rgb, tuple):
            raise ColorInputError(f"rgb should be of type 'tuple' but '{type(self.rgb).__name__}' given.")
        if len(tuple) != 3:
            raise ColorInputError(f"Expected (r, g, b) but given {self.rgb}")
        if self.rgb:
            for code in self.rgb:
                if code < 0 or code > 255:
                    raise ColorInputError(f"{self.rgb} is not a valid rgb color code.")
            return True

    def _convert_rgb_to_hex(self):
        return f"#{self.rgb[0]:02x}{self.rgb[1]:02x}{self.rgb[2]:02x}"

    def compile(self):
        if self.hex:
            return f'"{self.hex}"'
        if self.rgb:
            return self._convert_rgb_to_hex()
