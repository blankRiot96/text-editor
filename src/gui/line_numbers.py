import pygame

from src import window
from src.gui.stack import Align, Stack


class LineNumbers(Stack):
    def __init__(self) -> None:
        super().__init__([], Align.HORIZONTAL, padding=2)

        self.width = 10

    def draw(self, pos) -> None:
        super().draw(pos)
        pygame.draw.rect(window.surface, "yellow", (pos, (self.width, self.height)), width=2)
