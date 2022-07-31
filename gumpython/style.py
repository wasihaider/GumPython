from command import GumCommand
from run_command import run_command


class Style(GumCommand):
    def __int__(self, text):
        self.command.append("style")
        self.text = text

    def run(self):
        self.command.append(self.text)
        run_command(self.command)

    def add_border(self, border_type: str):
        self.command.extend(["--border", border_type])
        return self


