from pydantic import BaseModel


class COLORS:
    dark_black = "#252a34"
    black = "#2e3440"
    white = "#e5e9f0"
    grey = "#d8dee9"
    red = "#bf616a"
    frost_green = "#8fbcbb"
    cyan = "#88c0d0"
    green = "#a3be8c"
    yellow = "#ebcb8b"
    blue = "#81a1c1"
    magenta = "#b48ead"
    orange = "#d08770"



keybindings = {}

class Settings(BaseModel):
    keybindings: dict = keybindings
    
    BACKGROUND: str = COLORS.black
    BAR_BACKGROUND: str = COLORS.black
    WORKSPACES_BACKGROUND: str = COLORS.black
    TODOS_BACKGROUND: str = COLORS.black
    BORDER_DIM: str = COLORS.grey + " 50%"
    BORDER_LIT: str = COLORS.blue
    BORDER_TITLE_DIM: str = COLORS.grey, COLORS.dark_black
    BORDER_TITLE_LIT: str = COLORS.white, COLORS.blue
    SEARCH_COLOR: str = COLORS.red
    YANK_COLOR: str = COLORS.blue
    SAVE_ON_ESCAPE: bool = False
    USE_DAY_FIRST: bool = True
    DATE_FORMAT: str = "%d %h"
    TIME_FORMAT: str = "%H:%M"
    

global_settings = Settings()