import pygame

surface: pygame.Surface
events: list[pygame.Event]
width: int
height: int

GUI_STACK_CHANGED = pygame.event.custom_type()
