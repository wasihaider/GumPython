from gumpython.arguments import FormatArguments
from gumpython.exceptions import FormatArgumentError

from .command import GumCommand


class Format(GumCommand):
    def __init__(self, text):
        super(Format, self).__init__()
        self.argument = "format"
        self.arguments = FormatArguments()
        self.text = text
        self._validate_text()

    def _validate_text(self):
        if not isinstance(self.text, str):
            raise FormatArgumentError(
                f"'text' should be of type 'str' but '{type(self.text).__name__}' given."
            )

    def _compile_command(self):
        super(Format, self)._compile_command()
        self.command.append(self.text)

    def type(self, format_type: str):
        self._add_to_flag_set(self.arguments.type.type, format_type)
        return self
