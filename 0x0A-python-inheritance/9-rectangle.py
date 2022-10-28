#!/usr/bin/python3
"""Module 9-rectangle.
Creates a Rectangle class.
"""


BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    Private instance attributes:
        - width
        - height
    Public method area().
    Inherits from BaseGeometry.
    """

    def _init_(self, width, height):
        """Initializes an instance.
        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def _str_(self):
        """Returns a formatted string."""

        return str("[Rectangle] {}/{}".format(self._width, self._height))

    def area(self):
        """Computes the area of the Rectangle instance.
        Overwrites the area() method from BaseGeometry.
        """

        return self._width * self._height
