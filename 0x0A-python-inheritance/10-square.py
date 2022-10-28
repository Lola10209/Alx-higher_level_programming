#!/usr/bin/python3
"""Module 10-square.
Creates a Square class.
"""


BaseGeometry = _import_('7-base_geometry').BaseGeometry
Rectangle = _import_('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square.
    Private instance attribute size.
    Public method area().
    Inherits from Rectangle.
    """

    def _init_(self, size):
        """Initializes a Square.
        Args:
            - size: size of the square
        """

        self.integer_validator("size", size)
        super()._init_(size, size)
        self.__size = size

    def _str_(self):
        return super()._str_()

    def area(self):
        """Computes the area of a Square instance.
        Overwrites the area() method from Rectangle.
        """

        return self.__size ** 2
