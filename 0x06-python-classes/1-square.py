#!/usr/bin/python3
# 1-square.py
"""Square class to represent a square."""


class Square:
    """
    Defines a square and its basic properties

    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size: int) -> None:
        """
        Initialize the size of the square

        :param size: int size of square
        """
        self.__size = size
