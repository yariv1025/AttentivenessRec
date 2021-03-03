class Location:
    """
    Constructor:
    :param x - x coordinate of the upper right corner (0 on default).
    :param y - y coordinate of the upper right corner (0 on default).
    :param width - frame width (0 on default)
    :param length - frame length (0 on default)
    """

    def __init__(self, x=0, y=0, width=0, length=0):
        self.x = x
        self.y = y
        self.width = width
        self.length = length

    """
    Setter:
    :param int - x coordinate of the upper right corner.
    :param int - y coordinate of the upper right corner.
    :param float - frame width.
    :param float - frame length.
    """

    def set_location(self, x, y, width, length):
        self.x = x
        self.y = y
        self.width = width
        self.length = length

    """
    Getter:
    :return - returns Location object (x,y, width, length).
    """

    def get_location(self):
        location = Location(self.x, self.y, self.width, self.length)
        return location

    """
    :return - returns Location as a string.
    """

    def to_string(self):
        return '({0}, {1}, {2}, {3})'.format(self.x, self.y, self.width, self.length)
        # return '(x=%d, y=%d, width=%d, length=%d)' % (self.x, self.y, self.width, self.length)