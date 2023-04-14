#!/usr/bin/python3
"""
contains the class BaseGeometry and subclass Rectangle
"""


BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def _init_(self,width,height):
        """instatation of the rectange"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

