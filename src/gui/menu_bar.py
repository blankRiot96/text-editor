import pygame

from src import window
from src.gui.stack import Align, Stack


class MenuBar(Stack):
    def __init__(self) -> None:
        super().__init__([], Align.HORIZONTAL, padding=2)

        self.width = 30

    def draw(self, pos) -> None:
        super().draw(pos)
        pygame.draw.rect(window.surface, "red", (pos, (self.width, self.height)), width=2)
