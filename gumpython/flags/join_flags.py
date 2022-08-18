from gumpython.constants import FlagTypeChoice

from .flags import Flag


class JoinTextFlag:
    def __init__(self):
        self.align = Flag(name="align", type=FlagTypeChoice.ALIGN)
        self.horizontal = Flag(name="horizontal", type=FlagTypeChoice.BOOL)
        self.vertical = Flag(name="vertical", type=FlagTypeChoice.BOOL)
