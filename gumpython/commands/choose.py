from .command import GumCommand
from gumpython.arguments import ChooseArgument


class Choose(GumCommand):
    def __init__(self, item_list):
        super().__init__()
        self.argument = "choose"
        self.item_list = item_list
        self.arguments = ChooseArgument()

    def _compile_command(self):
        super(Choose, self)._compile_command()
        self.command.extend(self.item_list)

    def cursor(self, cursor_text: str, prefix: str = None):
        self._add_to_flag_set(self.arguments.cursor.cursor, cursor_text)
        if prefix:
            self._add_to_flag_set(self.arguments.cursor.prefix, prefix)
        return self

    def cursor_align(self, alignment: str, margin: tuple = None, padding: tuple = None):
        cursor = self.arguments.cursor
        self._add_to_flag_set(cursor.align, alignment)
        if margin:
            self._add_to_flag_set(cursor.margin, margin)
        if padding:
            self._add_to_flag_set(cursor.padding, padding)
        return self

    def cursor_color(self, foreground_color: str, background_color: str = None):
        cursor = self.arguments.cursor
        self._add_to_flag_set(cursor.foreground, foreground_color)
        if background_color:
            self._add_to_flag_set(cursor.background, background_color)
        return self

    def cursor_style(self, bold: bool = False, italic: bool = False, faint: bool = False, underline: bool = False,
                     strikethrough: bool = False, ):
        cursor = self.arguments.cursor
        if bold:
            self._add_to_flag_set(cursor.bold, None)
        if italic:
            self._add_to_flag_set(cursor.italic, None)
        if faint:
            self._add_to_flag_set(cursor.faint, None)
        if underline:
            self._add_to_flag_set(cursor.underline, None)
        if strikethrough:
            self._add_to_flag_set(cursor.strikethrough, None)
        return self

    def cursor_border(self, style: str, foreground_color: str = None, background_color: str = None):
        cursor = self.arguments.cursor
        self._add_to_flag_set(cursor.border, style)
        if foreground_color:
            self._add_to_flag_set(cursor.border_foreground, foreground_color)
        if background_color:
            self._add_to_flag_set(cursor.border_background, background_color)
        return self

    def size(self, width: int = None, height: int = None):
        cursor = self.arguments.cursor
        if width:
            self._add_to_flag_set(cursor.width, width)
        if height:
            self._add_to_flag_set(cursor.height, height)
        return self
