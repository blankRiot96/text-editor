import pygame
from pygame.typing import Point

from src import window


class HorizontalScrollBar:
    def __init__(self) -> None:
        self.width = 0
        self.height = 20
        self.fill_available_space = False
        self.hidden = False

    def on_input(self):
        for event in window.events:
            if event.type == window.SHOW_MENU_SCREEN:
                self.hidden = True

    def draw(self, pos: Point):
        pygame.draw.rect(window.surface, "blue", (pos, (self.width, self.height)), width=2)


class VerticalScrollBar:
    def __init__(self) -> None:
        self.width = 20
        self.height = 0
        self.fill_available_space = False
        self.hidden = False

    def on_input(self):
        for event in window.events:
            if event.type == window.SHOW_MENU_SCREEN:
                self.hidden = True

    def draw(self, pos: Point):
        pygame.draw.rect(window.surface, "blue", (pos, (self.width, self.height)), width=2)
