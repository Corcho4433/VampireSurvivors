"""Module that contains custom exceptions."""


class DeadPlayerException(Exception):
    """Exception raised when the player dies."""


class InvalidStatValueException(Exception):
    """Exception raised when an invalid value is given to a stat"""

    def __init__(self, msg):
        self.message = msg
