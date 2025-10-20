import pygame

from src import window


class FileTree:
    def __init__(self) -> None:
        self.width = 200
        self.height = 0
        self.fill_available_space = False
        self.hidden = False

    def on_input(self):
        for event in window.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and (event.mod & pygame.KMOD_CTRL):
                    self.hidden = not self.hidden
                    pygame.event.post(pygame.Event(window.GUI_STACK_CHANGED))

    def draw(self, pos) -> None:
        pygame.draw.rect(window.surface, "cyan", (pos, (self.width, self.height)), width=2)
