from gumpython.constants import FlagTypeChoice
from gumpython.run_command import run_command


class GumCommand:
    def __init__(self):
        self.command = None
        self.argument = None
        self.__flag_set = set()
        self.returning = False
        self.input = None

    def run(self):
        self._compile_command()
        response = run_command(self.command, self.input)
        if self.returning:
            return response.stdout
        print(response.stdout)

    def get_command(self):
        self._compile_command()
        return " ".join(self.command)

    def _add_to_flag_set(self, flag, value):
        if flag.type != FlagTypeChoice.BOOL:
            flag.value = value
        self.__flag_set.add(flag)

    def _compile_command(self):
        self.command = ["gum", self.argument]
        for flag in self.__flag_set:
            if flag.type == FlagTypeChoice.BOOL:
                self.command.append(flag.flag)
            else:
                self.command.append(flag.get_command())

    def _align(self, flag, alignment, margin=None, padding=None):
        self._add_to_flag_set(flag.align, alignment)
        if margin:
            self._add_to_flag_set(flag.margin, margin)
        if padding:
            self._add_to_flag_set(flag.padding, padding)

    def _border(
        self, flag, style, foreground_color=None, background_color=None
    ):
        self._add_to_flag_set(flag.border, style)
        if foreground_color:
            self._add_to_flag_set(flag.border_foreground, foreground_color)
        if background_color:
            self._add_to_flag_set(flag.border_background, background_color)

    def _color(self, flag, foreground, background=None):
        self._add_to_flag_set(flag.foreground, foreground)
        if background:
            self._add_to_flag_set(flag.background, background)

    def _font_style(
        self,
        flag,
        bold: bool = False,
        italic: bool = False,
        faint: bool = False,
        underline: bool = False,
        strikethrough: bool = False,
    ):
        if bold:
            self._add_to_flag_set(flag.bold, True)
        if faint:
            self._add_to_flag_set(flag.faint, True)
        if italic:
            self._add_to_flag_set(flag.italic, True)
        if underline:
            self._add_to_flag_set(flag.underline, True)
        if strikethrough:
            self._add_to_flag_set(flag.strikethrough, True)

    def _size(self, flag, width: int = None, height: int = None):
        if width:
            self._add_to_flag_set(flag.width, width)
        if height:
            self._add_to_flag_set(flag.height, height)

    def __str__(self):
        return self.get_command()
