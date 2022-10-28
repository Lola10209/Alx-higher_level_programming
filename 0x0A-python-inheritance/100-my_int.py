#!/usr/bin/python3
"""Module 100-my_int.
Creates a class that inherits from int.
"""


class MyInt(int):
    """Class inheriting from int,
    But reverses the behavior of != and ==.
    """

    def _eq_(self, other):
        """Equality becomes inequality."""

        return super()._ne_(other)

    def _ne_(self, other):
        """Inequality becomes equality."""

        return super()._eq_(other)
