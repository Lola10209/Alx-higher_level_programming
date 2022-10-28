#!/usr/bin/python3
"""Module 2-is_same_class
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class
    Args:
        obj (object): _description
        a_class (class): description
    Returns:
        True: if object is an instance of class
        False: if it is not
    """

    return True if type(obj) is a_class else False
