import pygame

from src import window


class TextBuffer:
    def __init__(self) -> None:
        self.width = 0
        self.height = 0

        self.fill_available_space = True
        self.hidden = False

    def on_input(self):
        pass

    def draw(self, pos) -> None:
        pygame.draw.rect(window.surface, "orange", (pos, (self.width, self.height)), width=2)
