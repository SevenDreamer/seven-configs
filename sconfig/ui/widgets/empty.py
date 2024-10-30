from rich.console import RenderableType
from rich.align import Align
from rich.console import Group
from textual.widget import Widget
from rich.text import Text

from enum import Enum

class EmptyWidgetType(Enum):
    dashboard="dashboard"

class EmptyWidget(Widget):
    def __init__(self):
        super().__init__()
        
    
    def render(self) -> RenderableType:
        return Align.center(
            Group(*[Align.center(Text.from_markup(str("this is empty")))])
        )