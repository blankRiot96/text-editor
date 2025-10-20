import pygame

from src import window
from src.gui.stack import Align, Stack


class Tabs(Stack):
    def __init__(self) -> None:
        super().__init__([], Align.HORIZONTAL)
        self.width = 0
        self.height = 40
        self.hidden = False
        self.fill_available_space = False

    def on_input(self):
        if not self.widgets:
            pygame.event.post(pygame.Event(window.SHOW_MENU_SCREEN))
            pygame.event.post(pygame.Event(window.GUI_STACK_CHANGED))
            self.hidden = True

    def draw(self, pos) -> None:
        # super().draw(pos)
        pygame.draw.rect(window.surface, "springgreen", (pos, (self.width, self.height)), width=2)
