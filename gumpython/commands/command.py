import subprocess
from gumpython.run_command import run_command


class GumCommand:
    def __init__(self):
        self.command = ["gum"]

    def run(self):
        run_command(self.command)

    def add_argument(self, name):
        self.command.append(name)

    def _update_command(self, flag, value):
        flag.value = value
        self.command.extend(flag.get_command())

    def __str__(self):
        return " ".join(self.command)
