import subprocess
from gumpython.run_command import run_command


class GumCommand:
    def __init__(self):
        self.command = None
        self.argument = None
        self.__flag_set = set()

    def run(self):
        self._compile_command()
        run_command(self.command)

    def _add_to_flag_set(self, flag, value):
        flag.value = value
        self.__flag_set.add(flag)

    def _compile_command(self):
        self.command = ["gum", self.argument]
        for flag in self.__flag_set:
            self.command.append(flag.get_command())

    def __str__(self):
        return " ".join(self.command)
