from typing import List, Union

from gumpython.arguments import StyleArgument
from gumpython.exceptions import StyleArgumentError
from gumpython.style import GumStyle

from .command import GumCommand


class Style(GumCommand):
    def __init__(
        self, text: Union[str, List[str]], gum_style_object: GumStyle
    ):
        super().__init__()
        self.argument = "style"
        self.text = text
        self._validate_text_argument()
        self.arguments = StyleArgument()
        self.gum_style_object = gum_style_object

    def _compile_command(self):
        self._compile_style(self.gum_style_object, self.arguments.args)
        super(Style, self)._compile_command()
        if isinstance(self.text, str):
            self.command.append(self.text)
        if isinstance(self.text, list):
            self.command.extend(self.text)

    def _validate_text_argument(self):
        if isinstance(self.text, str):
            return True
        if isinstance(self.text, list):
            for t in self.text:
                if not isinstance(t, str):
                    raise StyleArgumentError(f"{t} is not a string.")
            return True
        raise StyleArgumentError(
            f"Expected 'str' or List[str] but '{type(self.text).__name__}' is given."
        )

    def get_command(self):
        self._compile_style(self.gum_style_object, self.arguments.args)
        super(Style, self)._compile_command()
        if isinstance(self.text, str):
            self.command.append(f"'{self.text}'")
        if isinstance(self.text, list):
            self.command.extend(list(map(lambda x: f"'{x}'", self.text)))
        return " ".join(self.command)
