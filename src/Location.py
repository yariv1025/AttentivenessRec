"""
:return Boolean
checks for valid value
"""


def check_value(value):
    if (not isinstance(value, int)) or value < 0:
        return False
    return True


"""
:return Boolean
checks for valid values
"""


def check_multi_value(*integers):
    for x in integers:
        if not check_value(x):
            return False
    return True


class Location:


    def __init__(self, x=0, y=0, width=0, length=0):
        """
        Constructor:
        :param x - x coordinate of the upper right corner (0 on default).
        :param y - y coordinate of the upper right corner (0 on default).
        :param width - frame width (0 on default)
        :param length - frame length (0 on default)
        """
        if not check_multi_value(x, y, width, length):
            raise IOError("Invalid values")
        self.x = x
        self.y = y
        self.width = width
        self.length = length



    def set_x(self, x):
        """
        Set x coordinate value.
        :param int - x coordinate of the upper right corner.
        """
        if not check_value(x):
            raise IOError("Invalid values")
        self.x = x
        return True

    """
    :param int - y coordinate of the upper right corner.
    """

    def set_y(self, y):
        if not check_value(y):
            raise IOError("Invalid values")
        self.y = y
        return True

    """
    :param int - frame width.
    """

    def set_width(self, width):
        if not check_value(width):
            raise IOError("Invalid values")
        self.width = width
        return True

    """    
    :param int - frame length.
    """

    def set_length(self, length):
        if not check_value(length):
            raise IOError("Invalid values")
        self.length = length
        return True

    """
    :return - returns Location object (x,y, width, length).
    """

    def get_location(self):
        return {'x': self.x,
                'y': self.y,
                'width': self.width,
                'length': self.length
                }

    """
    :return - returns Location as a string.
    """

    def to_string(self):
        return '({0}, {1}, {2}, {3})'.format(self.x, self.y, self.width, self.length)