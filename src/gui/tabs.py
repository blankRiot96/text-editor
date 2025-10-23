from pathlib import Path

import pygame
from pygame.typing import Point

from src import window
from src.gui import utils
from src.gui.stack import Align, Stack


class CloseTabButton:
    def __init__(self) -> None:
        self.width = 40
        self.height = 40

    def on_input(self) -> None:
        pass

    def draw(self) -> None:
        pass


class Tab:
    height = 40

    def __init__(self, file_path: str | None) -> None:
        self.width = 200
        self.fill_available_space = False
        self.hidden = False
        self.close_button = CloseTabButton()

        # self.file_path = None if file_path is None else Path(file_path)
        self.file_path = Path("pyproject.toml")
        self.regular_font = utils.load_font("assets/fonts/maple/MapleMono-Regular.ttf", 16)
        self.italized_font = utils.load_font("assets/fonts/maple/MapleMono-Italic.ttf", 16)
        self.name_surface = self.generate_name_surface()
        self.name_rect = self.name_surface.get_rect()

    def is_file_name_too_long(self, file_name: str) -> bool:
        available_space = self.width - self.close_button.width
        uncut_name_surface = self.regular_font.render(file_name, True, "white")

        return available_space - uncut_name_surface.width < 0

    def get_maximum_file_name_length(self, file_name: str) -> int:
        # Works only for mono-fonts
        one_char_width = self.regular_font.render(" ", True, "white").width
        available_space = self.width - self.close_button.width

        return int(available_space / one_char_width)

    def cut_file_name(self, file_name: str) -> str:
        max_len = self.get_maximum_file_name_length(file_name)
        return file_name[: max_len - 3] + "..."

    def generate_name_surface(self) -> pygame.Surface:
        if self.file_path is None:
            return self.italized_font.render("untitled", True, "white")

        if self.is_file_name_too_long(self.file_path.name):
            return self.regular_font.render(self.cut_file_name(self.file_path.name), True, "white")

        return self.regular_font.render(self.file_path.name, True, "white")

    def on_input(self):
        self.close_button.on_input()

    def draw(self, pos: Point):
        rect = pygame.Rect(pos, (self.width, self.height))
        pygame.draw.rect(window.surface, "white", rect, width=2)
        self.name_rect.midleft = rect.midleft + pygame.Vector2(10, 0)
        window.surface.blit(self.name_surface, self.name_rect)

        self.close_button.draw()


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
