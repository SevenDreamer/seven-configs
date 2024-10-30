from typer import Typer

from sconfig.ui.tui import Sconfig
app = Typer(
    no_args_is_help=True
)

@app.command("ui")
def open_ui():
    Sconfig().run()

@app.command("add")
def add_config():...

if __name__ == "__main__":
    app()