#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """A subclass of list"""
    def _init_(self):
        """initializes the object"""
        super()._int_()

    def print_sorted(self):
        """prints sorted list""""
        print (sorted(self))

