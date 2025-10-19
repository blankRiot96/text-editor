import pygame

from src import window
from src.gui.file_tree import FileTree
from src.gui.line_numbers import LineNumbers
from src.gui.menu_bar import MenuBar
from src.gui.scroll_bar import HorizontalScrollBar, VerticalScrollBar
from src.gui.stack import Align, Stack
from src.gui.text_buffer import TextBuffer


class App:
    def __init__(self) -> None:
        pygame.init()
        window.surface = pygame.display.set_mode((1200, 800), pygame.RESIZABLE, vsync=1)
        window.width, window.height = window.surface.get_size()

        # self.window_container = Stack(
        #     [
        #         MenuBar(),
        #         Stack(
        #             [
        #                 FileTree(),
        #                 LineNumbers(),
        #                 Stack([TextBuffer(), HorizontalScrollBar()], Align.HORIZONTAL),
        #                 VerticalScrollBar(),
        #             ],
        #             Align.HORIZONTAL,
        #         ),
        #     ],
        #     Align.VERTICAL,
        #     padding=20,
        # )

        self.window_container = Stack([FileTree(), TextBuffer()], Align.HORIZONTAL, padding=20)

        self.resize_window()
        self.running = True

    def resize_window(self):
        self.window_container.width = window.width
        self.window_container.height = window.height
        self.window_container.resize_child_stacks()

    def on_input(self):
        window.events = pygame.event.get()
        for event in window.events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                window.width, window.height = window.surface.get_size()
                self.resize_window()

        self.window_container.on_input()

    def draw(self):
        window.surface.fill("black")
        self.window_container.draw((0, 0))
        pygame.display.flip()

    def run(self):
        while self.running:
            self.on_input()
            self.draw()
            # break
