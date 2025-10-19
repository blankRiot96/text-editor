import pygame

from src import window
from src.gui.stack import Align, Stack


class MenuBar:
    def __init__(self) -> None:
        # super().__init__([], Align.HORIZONTAL, padding=2, fill=False)

        self.width = 0
        self.height = 30
        self.fill_available_space = False
        self.hidden = False

    def on_input(self): ...

    def draw(self, pos) -> None:
        # super().draw(pos)
        pygame.draw.rect(window.surface, "red", (pos, (self.width, self.height)), width=2)
