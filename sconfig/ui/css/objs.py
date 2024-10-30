from . import global_settings

BG = global_settings.BACKGROUND
DIM = global_settings.BORDER_DIM
BORDER_TITLE_DIM = global_settings.BORDER_TITLE_DIM
if not isinstance(BORDER_TITLE_DIM, tuple):
    BORDER_TITLE_DIM = BORDER_TITLE_DIM, DIM

OBJS = f"""
* {{
    link-style: italic;
    link-style-hover: underline italic bold;
    link-background-hover: #fff 0%;
}}

MainScreen {{
    background: {BG};
    layout: vertical;
}}

DualSplit {{
    layout: grid;
    grid-size: 2;
    grid-columns: 2fr 8fr;
}}

EmptyWidget {{
    background: {BG};
    border: {DIM};
    border-title-background:{BORDER_TITLE_DIM[1]};
    border-title-color: {BORDER_TITLE_DIM[0]};
    padding: 1;
    width: 100%;
    height: 100%;
    layer: L2;
}}


"""