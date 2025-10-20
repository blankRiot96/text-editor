import pygame

surface: pygame.Surface
events: list[pygame.Event]
width: int
height: int

GUI_STACK_CHANGED = pygame.event.custom_type()
SHOW_MENU_SCREEN = pygame.event.custom_type()
HIDE_MENU_SCREEN = pygame.event.custom_type()
