from pathlib import Path

import pygame
from pygame.typing import Point

from src import window
from src.gui import utils
from src.gui.stack import Align, Stack


class Tab:
    height = 40

    def __init__(self, file_path: str | None) -> None:
        self.file_path = None if file_path is None else Path(file_path)
        self.regular_font = utils.load_font("assets/fonts/maple/MapleMono-Regular.ttf", 16)
        self.italized_font = utils.load_font("assets/fonts/maple/MapleMono-Italic.ttf", 16)
        self.name_surface = self.generate_name_surface()
        self.name_rect = self.name_surface.get_rect()

        self.width = 150
        self.height = 40
        self.fill_available_space = False
        self.hidden = False

    def generate_name_surface(self) -> pygame.Surface:
        if self.file_path is None:
            return self.italized_font.render("untitled", True, "white")
        return self.regular_font.render(self.file_path.name, True, "white")

    def on_input(self): ...

    def draw(self, pos: Point):
        rect = pygame.Rect(pos, (self.width, self.height))
        pygame.draw.rect(window.surface, "white", rect, width=2)
        self.name_rect.midleft = rect.midleft + pygame.Vector2(10, 0)
        window.surface.blit(self.name_surface, self.name_rect)


class Tabs(Stack):
    def __init__(self) -> None:
        super().__init__([], Align.HORIZONTAL)
        self.width = 0
        self.height = Tab.height
        self.hidden = False
        self.fill_available_space = False

    def on_input(self):
        for event in window.events:
            if event.type == window.ACTIVE_FILE_CHANGED:
                if event.dict["file-path"] is None:
                    self.widgets.append(Tab(None))

        if not self.widgets:
            pygame.event.post(pygame.Event(window.SHOW_MENU_SCREEN))
            pygame.event.post(pygame.Event(window.GUI_STACK_CHANGED))
            self.hidden = True

    def draw(self, pos) -> None:
        super().draw(pos)
        pygame.draw.rect(window.surface, "springgreen", (pos, (self.width, self.height)), width=2)
