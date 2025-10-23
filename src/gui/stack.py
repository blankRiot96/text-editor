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
    hidden: bool

    def on_input(self) -> None: ...
    def draw(self, pos: Point) -> None: ...


class Stack:
    def __init__(
        self,
        widgets: list[StackableWidget],
        alignment: Align,
        padding: int = 0,
    ) -> None:
        self.all_widgets = widgets
        self.populate_widgets()
        self.alignment = alignment
        self.padding = padding

        self.fill_available_space = True
        self.hidden = False

        # Needs to be set by uppermost stack and calling `resize_child_stacks`
        self.width = 0
        self.height = 0

    def populate_widgets(self):
        self.widgets: list[StackableWidget] = [w for w in self.all_widgets if not w.hidden]

    def get_max_child_width(self) -> int:
        return max(
            self.widgets, key=lambda w: w.get_max_child_width() if isinstance(w, Stack) else w.width
        ).width

    def get_max_child_height(self) -> int:
        return max(
            self.widgets,
            key=lambda w: w.get_max_child_height() if isinstance(w, Stack) else w.height,
        ).height

    def resize_child_stacks(self):
        for widget in self.widgets:
            if self.alignment == Align.VERTICAL:
                widget.width = self.width
                # widget.height = self.get_max_child_height()
            else:
                widget.height = self.height
                # widget.width = self.get_max_child_width()

        self.expand_filler_widgets()

        for widget in self.widgets:
            if isinstance(widget, Stack):
                widget.resize_child_stacks()

    def expand_filler_widgets(self):
        filler_widgets = []
        static_widgets = []
        for widget in self.widgets:
            if widget.fill_available_space:
                filler_widgets.append(widget)
            else:
                static_widgets.append(widget)

        if not filler_widgets:
            return

        n = len(filler_widgets)

        if self.alignment == Align.VERTICAL:
            space_by_static_widgets = sum(w.height for w in static_widgets) + self.padding * len(
                static_widgets
            )
            available_space = self.height - space_by_static_widgets
            for widget in filler_widgets:
                widget.height = int(available_space / n)
        elif self.alignment == Align.HORIZONTAL:
            space_by_static_widgets = sum(w.width for w in static_widgets) + self.padding * len(
                static_widgets
            )
            available_space = self.width - space_by_static_widgets
            for widget in filler_widgets:
                widget.width = int(available_space / n)

    def on_input(self):
        for widget in self.all_widgets:
            widget.on_input()

        self.populate_widgets()

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
