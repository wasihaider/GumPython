from gumpython.constants import FlagTypeChoice
from gumpython.exceptions import InputError
from gumpython.run_command import run_command
from gumpython.style import GumStyle, get_styles


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
        else:
            if not isinstance(value, bool):
                raise InputError(
                    f"'bool' expected for {flag.display_name} but '{type(value).__name__}' given."
                )
            if value:
                self.__flag_set.add(flag)

    def _compile_style(self, style: GumStyle, flag):
        styles = get_styles(style)
        for style, value in styles.items():
            self._add_to_flag_set(getattr(flag, style), value)

    def _compile_command(self):
        self.command = ["gum", self.argument]
        for flag in self.__flag_set:
            if flag.type == FlagTypeChoice.BOOL:
                self.command.append(flag.flag)
            else:
                self.command.append(flag.get_command())

    def __str__(self):
        return self.get_command()
