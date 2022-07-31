from command import GumCommand
from run_command import run_command
from flags import Flag

class StyleFlag(Flag):
    data: str


class Style(GumCommand):
    def __int__(self, text):
        self.command.append("style")
        self.text = text

    def run(self):
        self.command.append(self.text)
        run_command(self.command)

    def add_border(self, style: str, background_color=None, foreground_color=None, ):
        border_styles = ["--border", style]
        if background_color:
            border_styles.extend(["--border-background", background_color])
        if foreground_color:
            border_styles.extend(["--border-foreground", foreground_color])
        return self

    def


