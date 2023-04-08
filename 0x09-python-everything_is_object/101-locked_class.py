#!/usr/bin/python3
class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance attributes,
    except for the attribute called first_name.
    """
    __slots__ = ['first_name']
        
        def __init__(self):
        """ Init method """
        pass
