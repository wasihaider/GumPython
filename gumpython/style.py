from dataclasses import asdict, dataclass, field, fields
from typing import Union


@dataclass
class Border:
    border: str = None
    border_foreground: Union[str, tuple] = None
    border_background: Union[str, tuple] = None


@dataclass
class Alignment:
    align: str = None
    margin: tuple = None
    padding: tuple = None


@dataclass
class Color:
    foreground: Union[str, tuple] = None
    background: Union[str, tuple] = None


@dataclass
class FontStyle:
    bold: bool = False
    italic: bool = False
    faint: bool = False
    underline: bool = False
    strikethrough: bool = False


@dataclass
class Size:
    width: int = None
    height: int = None


@dataclass
class GumStyle:
    border: Border = field(default_factory=Border)
    alignment: Alignment = field(default_factory=Alignment)
    color: Color = field(default_factory=Color)
    font_style: FontStyle = field(default_factory=FontStyle)
    size: Size = field(default_factory=Size)


def get_styles(style: GumStyle):
    styles = {}
    for f in fields(style):
        attr = getattr(style, f.name)
        styles.update(
            asdict(
                attr,
                dict_factory=lambda x: {k: v for (k, v) in x if v is not None},
            )
        )
    return styles
