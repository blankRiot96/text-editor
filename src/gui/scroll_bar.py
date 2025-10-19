from pygame.typing import Point


class HorizontalScrollBar:
    width: int
    height: int

    def on_input(self): ...
    def draw(self, pos: Point): ...


class VerticalScrollBar:
    width: int
    height: int

    def on_input(self): ...
    def draw(self, pos: Point): ...
