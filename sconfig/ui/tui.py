from textual.app import App
from sconfig.ui.css.main import screen_CSS
from sconfig.ui.screens import MainScreen
from sconfig.utils.watcher import Watcher
class Sconfig(App):
    CSS = screen_CSS
    
    SCREENS = {
        "main": MainScreen(name="main")
    }
    
    async def on_mount(self):
        self.watch = Watcher()
        self.push_screen("main")