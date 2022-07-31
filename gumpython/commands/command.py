import subprocess
from gumpython.run_command import run_command


class GumCommand:
    def __init__(self):
        self.command = ["gum"]

    def run(self):
        run_command(self.command)

    def __str__(self):
        return " ".join(self.command)
