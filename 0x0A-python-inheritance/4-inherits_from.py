!/usr/bin/python3
"""
contains the function of inherits_from
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, else flase"""
    return (issubclass(type(obj), a_class) and (type(obj) != a_class)
