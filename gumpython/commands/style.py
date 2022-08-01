from .command import GumCommand
from gumpython.run_command import run_command
from gumpython.arguments import StyleArgument


class Style(GumCommand):
    def __init__(self, text):
        super().__init__()
        self.add_argument("style")
        self.text = text
        self.arguments = StyleArgument()

    def run(self):
        # TODO: Fix - text appends on each time we call run
        self.command.append(self.text)
        run_command(self.command)

    def border(self, style: str = None, foreground_color: str = None, background_color: str = None, ):
        border = self.arguments.border
        if style:
            self._update_command(border.style, style)
        if background_color:
            self._update_command(border.background_color, background_color)
        if foreground_color:
            self._update_command(border.foreground_color, foreground_color)

    def align(self, alignment: str, margin: tuple = (0, 0), padding: tuple = (0, 0)):
        self._update_command(self.arguments.text.align, alignment)
        self._update_command(self.arguments.text.margin, margin)
        self._update_command(self.arguments.text.padding, padding)

    def text_color(self, foreground, background=None):
        self._update_command(self.arguments.text.foreground_color, foreground)
        if background:
            self._update_command(self.arguments.text.background_color, background)

    def text_font(self, bold: bool = False, faint: bool = False, italic: bool = False, underline: bool = False,
                  strikethrough: bool = False):
        text_arg = self.arguments.text
        if bold:
            self._update_command(text_arg.bold, None)
        if faint:
            self._update_command(text_arg.faint, None)
        if italic:
            self._update_command(text_arg.italic, None)
        if underline:
            self._update_command(text_arg.underline, None)
        if strikethrough:
            self._update_command(text_arg.strikethrough, None)

    def size(self, width: int, height: int = None):
        text_arg = self.arguments.text
        self._update_command(text_arg.width, width)
        if height:
            self._update_command(text_arg.height, height)
