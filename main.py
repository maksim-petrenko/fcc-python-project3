# https://www.freecodecamp.org/
# Curriculum: Python Certification
# Project: Build a Polygon Area Calculator
# Copyright (C) 2026 Maksim Petrenko


########################################################################
# Classes

class Rectangle:

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return (self.width * "*" + "\n") * self.height

    def get_amount_inside(self, shape: object) -> int:
        if self.width >= shape.width and self.height >= shape.height:
            return self.get_area() // shape.get_area()
        return 0


class Square(Rectangle):

    def __init__(self, side: int) -> None:
        self.width = self.height = side

    def __repr__(self) -> str:
        return f"Square(side={self.width})"

    def set_side(self, side: int) -> None:
        self.width = self.height = side

    def set_width(self, side: int) -> None:
        self.width = self.height = side

    def set_height(self, side: int) -> None:
        self.width = self.height = side
