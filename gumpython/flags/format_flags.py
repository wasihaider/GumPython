from gumpython.constants import FlagTypeChoice

from .flags import Flag


class FormatFlag:
    def __init__(self):
        self.type = Flag(name="type", type=FlagTypeChoice.FORMAT)
