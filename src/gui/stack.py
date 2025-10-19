import enum

import pygame
import typing_extensions as t
from pygame.typing import Point


class Align(enum.Enum):
    HORIZONTAL = enum.auto()
    VERTICAL = enum.auto()


class StackableWidget(t.Protocol):
    width: int
    height: int
    fill_available_space: bool

    def on_input(self) -> None: ...
    def draw(self, pos: Point) -> None: ...


class Stack:
    def __init__(
        self,
        widgets: list[StackableWidget],
        alignment: Align,
        padding: int = 0,
    ) -> None:
        self.widgets = widgets
        self.alignment = alignment
        self.padding = padding

        self.fill_available_space = False

        # Needs to be set by uppermost stack and calling `resize_child_stacks`
        self.width = 0
        self.height = 0

    def get_max_child_width(self) -> int:
        biggest_width = 0
        for widget in self.widgets:
            if isinstance(widget, Stack) and widget.width == 0:
                width = widget.get_max_child_width()
            else:
                width = widget.width

            if width > biggest_width:
                biggest_width = width

        return biggest_width

    def get_max_child_height(self) -> int:
        biggest_height = 0
        for widget in self.widgets:
            if isinstance(widget, Stack) and widget.height == 0:
                height = widget.get_max_child_height()
            else:
                height = widget.height

            if height > biggest_height:
                biggest_height = height

        return biggest_height

    def resize_child_stacks(self):
        for widget in self.widgets:
            if self.alignment == Align.VERTICAL:
                widget.width = self.width
                # widget.height = self.get_max_child_height()
            else:
                widget.height = self.height
                # widget.width = self.get_max_child_width()

            if isinstance(widget, Stack):
                widget.resize_child_stacks()

        self.expand_filler_widgets()

    def expand_filler_widgets(self):
        filler_widgets = [w for w in self.widgets if w.fill_available_space]
        if not filler_widgets:
            return

        n = len(filler_widgets)

        if self.alignment == Align.VERTICAL:
            available_space = (
                self.height - self.calculate_vertical_position((0, 0), len(self.widgets) - 1).y
            )
            for widget in filler_widgets:
                widget.height = int(available_space / n)
        elif self.alignment == Align.HORIZONTAL:
            available_space = (
                self.width - self.calculate_horizontal_position((0, 0), len(self.widgets) - 1).x
            )
            for widget in filler_widgets:
                widget.width = int(available_space / n)

    def on_input(self):
        for widget in self.widgets:
            widget.on_input()

    def calculate_horizontal_position(
        self, initial_position: Point, nth_widget: int
    ) -> pygame.Vector2:
        used_horizontal_space = 0
        for widget in self.widgets[:nth_widget]:
            used_horizontal_space += widget.width + self.padding

        x = initial_position[0] + used_horizontal_space

        return pygame.Vector2(x, initial_position[1])

    def calculate_vertical_position(
        self, initial_position: Point, nth_widget: int
    ) -> pygame.Vector2:
        used_vertical_space = 0
        for widget in self.widgets[:nth_widget]:
            used_vertical_space += widget.height + self.padding

        y = initial_position[1] + used_vertical_space

        return pygame.Vector2(initial_position[0], y)

    def draw(self, pos: Point) -> None:
        for nth_widget, widget in enumerate(self.widgets):
            if self.alignment == Align.HORIZONTAL:
                wpos = self.calculate_horizontal_position(pos, nth_widget)
            else:
                wpos = self.calculate_vertical_position(pos, nth_widget)
            widget.draw(wpos)
