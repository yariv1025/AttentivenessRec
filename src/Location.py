def check_value(value):
    """
    checks for valid value
    :param value: integer (0-255)
    :return: Boolean
    """
    if (not isinstance(value, int)) or value < 0:
        return False
    return True


def check_multi_value(*integers):
    """
    checks for multi valid values
    :param integers: integers (value: 0-255)
    :return: boolean
    """
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

    def set_y(self, y):
        """
        reset y coordinate of the upper right corner.
        :param y: integer - coordinate of the upper right corner.
        :return: boolean
        """
        if not check_value(y):
            raise IOError("Invalid values")
        self.y = y
        return True

    def set_width(self, width):
        """
        reset the width of the face box.
        :param width: integer - width of the face box
        :return: boolean
        """
        if not check_value(width):
            raise IOError("Invalid values")
        self.width = width
        return True

    def set_length(self, length):
        """
        reset the length of the face box.
        :param length: integer - length of the face box
        :return: boolean
        """
        if not check_value(length):
            raise IOError("Invalid values")
        self.length = length
        return True

    def get_location(self):
        """
        gets the Location object (x,y, width, length).
        :return: Location
        """
        return {'x': self.x,
                'y': self.y,
                'width': self.width,
                'length': self.length
                }

    def to_string(self):
        """
        create a readable string of Location object.
        :return: object string
        """
        return '({0}, {1}, {2}, {3})'.format(self.x, self.y, self.width, self.length)

