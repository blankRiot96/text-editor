import pygame

from src import window


class LineNumbers:
    def __init__(self) -> None:
        self.width = 40
        self.height = 0
        self.fill_available_space = False
        self.hidden = False

    def on_input(self): ...

    def draw(self, pos) -> None:
        pygame.draw.rect(window.surface, "yellow", (pos, (self.width, self.height)), width=2)
