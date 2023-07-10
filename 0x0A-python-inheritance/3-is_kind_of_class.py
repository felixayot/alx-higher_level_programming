#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
        Checks if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
