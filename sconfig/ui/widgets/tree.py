from textual.widget import Widget

class Tree(Widget):
    
    def __init__(self, model: Model, classes: str=""):
        super().__init__(id=f"Tree-{}")