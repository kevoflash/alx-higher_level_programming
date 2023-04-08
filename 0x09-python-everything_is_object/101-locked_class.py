class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance attributes,
    except for the attribute called first_name.
    """
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} does not support attribute assignment")
        self.__dict__[name] = value

