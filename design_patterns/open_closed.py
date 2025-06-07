from abc import ABC, abstractmethod
from typing import override


class ShapeCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.length * shape.width
        elif shape.type == "circle":
            return 3.14 * (shape.radius**2)

    def calculate_perimeter(self, shape):
        if shape.type == "rectangle":
            return 2*(shape.length + shape.width)
        elif shape.type == "circle":
            return 2*3.14 * shape.radius


# Create abstract base class for shapes and separate concrete class

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width*self.height

    def calculate_perimeter(self):
        return 2*(self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14*self.radius*self.radius

    def calculate_perimeter(self):
        return 2*3.14*self.radius