#!/usr/bin/python3
"""
contains the function is_kind_class
"""


def is_kind_of_class(obj, a_class):
    """True if obj is inherited from a_class, else false"""
    return(isinstance(obj, a_class))
