from gumpython.constants import FlagTypeChoice
from gumpython.exceptions import InputError
from gumpython.run_command import run_command
from gumpython.style import GumStyle, get_styles


# GumCommand is a class that represents a command that can be executed by the Gum CLI.
class GumCommand:
    def __init__(self):
        """
        This function initializes the command and argument variables to None, and creates a set of flags
        """
        self.command = None
        self.argument = None
        self.__flag_set = set()
        self.returning = False
        self.input = None

    def run(self):
        """
        It compiles the command, runs it, and returns the output if the user wants it

        :return: The output of the command.
        """
        self._compile_command()
        response = run_command(self.command, self.input)
        if self.returning:
            return response.stdout
        print(response.stdout)

    def get_command(self):
        """
        It takes the command that was passed to the constructor and adds the arguments that were passed to the constructor
        to the command

        :return: The command that will be used to run the program.
        """
        self._compile_command()
        return " ".join(self.command)

    def _add_to_flag_set(self, flag, value):
        """
        If the flag is not a boolean, then set the flag's value to the value passed in. If the flag is a boolean, then check
        if the value passed in is a boolean. If it is, then add the flag to the flag set

        :param flag: The flag object
        :param value: The value of the flag
        """
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
        """
        It takes a GumStyle object and a flag object, and it adds the styles from the GumStyle object to the flag object

        :param style: The style to compile
        :type style: GumStyle
        :param flag: The flag to add the style to
        """
        styles = get_styles(style)
        for style, value in styles.items():
            self._add_to_flag_set(getattr(flag, style), value)

    def _compile_command(self):
        """
        It takes the flags that have been set and adds them to the command that will be executed
        """
        self.command = ["gum", self.argument]
        for flag in self.__flag_set:
            if flag.type == FlagTypeChoice.BOOL:
                self.command.append(flag.flag)
            else:
                self.command.append(flag.get_command())

    def __str__(self):
        return self.get_command()
