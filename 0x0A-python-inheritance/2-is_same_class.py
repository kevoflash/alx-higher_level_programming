#!/usr/bin/python3
"""
contains the fuction is_same_class
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact a_class, otherwise false"""
    return(type(obj) == a_class)
