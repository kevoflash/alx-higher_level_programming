#!/usr/bin/python3
"""
Contains function that returns the JSON
representation of an object
"""

import json


def to_json_string(myobj):
    """"Function that returns the JSON representation of an object

    Args:
    myobj: object

    Raises:
    Exception: when the object can't be encoded

    """
   return json.loads(my_obj)
