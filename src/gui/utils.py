import functools

import pygame


@functools.lru_cache
def load_font(name: str | None, size: int) -> pygame.Font:
    return pygame.Font(name, size)
