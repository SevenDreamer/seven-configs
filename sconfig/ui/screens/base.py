from textual.app import events
from textual.screen import Screen

class BaseScreen(Screen):
    """
    具有将“Key”事件解析为 str 的功能的基本屏幕
    """