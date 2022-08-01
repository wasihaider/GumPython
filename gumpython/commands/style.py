from .command import GumCommand
from gumpython.run_command import run_command
from gumpython.arguments import StyleArgument


class Style(GumCommand):
    def __init__(self, text):
        super().__init__()
        self.argument = "style"
        self.text = text
        self.arguments = StyleArgument()

    def _compile_command(self):
        super(Style, self)._compile_command()
        self.command.append(self.text)

    def border(self, style: str = None, foreground_color: str = None, background_color: str = None, ):
        border = self.arguments.border
        if style:
            self._add_to_flag_set(border.style, style)
        if background_color:
            self._add_to_flag_set(border.background_color, background_color)
        if foreground_color:
            self._add_to_flag_set(border.foreground_color, foreground_color)

    def align(self, alignment: str, margin: tuple = (0, 0), padding: tuple = (0, 0)):
        self._add_to_flag_set(self.arguments.text.align, alignment)
        self._add_to_flag_set(self.arguments.text.margin, margin)
        self._add_to_flag_set(self.arguments.text.padding, padding)

    def text_color(self, foreground, background=None):
        self._add_to_flag_set(self.arguments.text.foreground_color, foreground)
        if background:
            self._add_to_flag_set(self.arguments.text.background_color, background)

    def text_font(self, bold: bool = False, faint: bool = False, italic: bool = False, underline: bool = False,
                  strikethrough: bool = False):
        text_arg = self.arguments.text
        if bold:
            self._add_to_flag_set(text_arg.bold, None)
        if faint:
            self._add_to_flag_set(text_arg.faint, None)
        if italic:
            self._add_to_flag_set(text_arg.italic, None)
        if underline:
            self._add_to_flag_set(text_arg.underline, None)
        if strikethrough:
            self._add_to_flag_set(text_arg.strikethrough, None)

    def size(self, width: int, height: int = None):
        text_arg = self.arguments.text
        self._add_to_flag_set(text_arg.width, width)
        if height:
            self._add_to_flag_set(text_arg.height, height)
