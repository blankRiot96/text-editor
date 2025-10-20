import pygame

from src import window


class MenuScreen:
    def __init__(self) -> None:
        self.width = 0
        self.height = 0
        self.fill_available_space = True
        self.hidden = True

    def on_input(self):
        for event in window.events:
            if event.type == window.SHOW_MENU_SCREEN:
                self.hidden = False

    def draw(self, pos) -> None:
        pygame.draw.rect(window.surface, "purple", (pos, (self.width, self.height)), width=2)
