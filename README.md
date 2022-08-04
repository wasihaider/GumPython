# GumPython
 A python library for gum cli

## Requirements

- [gum cli](https://github.com/charmbracelet/gum)
- Python >= 3.8

## How to Use

```python
from gumpython import Style, color, alignment, border

style = Style(["Hi there!", "My name is GumPython :)"]) \
            .border(border.ROUNDED, foreground_color=color.FUCHSIA) \
            .text_color(foreground=color.AQUA) \
            .align(alignment=alignment.CENTER) \
            .text_font(bold=True, italic=True)

style.run()
```