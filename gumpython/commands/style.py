from .command import GumCommand
from gumpython.run_command import run_command
from gumpython.arguments import StyleArgument


class Style(GumCommand):
    def __init__(self, text):
        super().__init__()
        self.command.append("style")
        self.text = text
        self.arguments = StyleArgument()

    def run(self):
        # TODO: Fix - text appends on each time we call run
        self.command.append(self.text)
        run_command(self.command)

    def add_border(self, style: str = None, background_color: str = None, foreground_color: str = None, ):
        border = self.arguments.border
        if style:
            border.style.value = style
            self.command.extend(border.style.get_command())
        if background_color:
            border.background_color.value = background_color
            self.command.extend(border.background_color.get_command())
        if foreground_color:
            border.foreground_color.value = foreground_color
            self.command.extend(border.foreground_color.get_command())
