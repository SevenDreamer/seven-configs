from textual.containers import Container
from .base import BaseScreen
from sconfig.ui.widgets.empty import EmptyWidget

class DualSplit(Container):...

class DualSplitLeft(Container):...

class DualSplitRight(Container):...

class MainScreen(BaseScreen):
    def compose(self):
        with DualSplit():
            with DualSplitLeft():
                yield EmptyWidget()
            with DualSplitRight():
                yield EmptyWidget()
        # with StatusBar()