"""Module that contains custom exceptions."""


class DeadPlayerException(Exception):
    """Exception raised when the player dies."""
    
class InvalidStatValueException(Exception):
    """Exception raised when an invalid value is given to a stat"""

    def __init__(self, msg):
        self.message = msg

class InvalidStatNameException(Exception):
    """Exception raised when an invalid value is given to a stat"""

class InvalidWeaponName(Exception):
    """Exception raised when an invalid weapon name is given to the factory"""

class InvalidPerkName(Exception):
    """Exception raised when an invalid perk name is given to the factory"""


class InvalidMovementSpeed(Exception):
    """Exception raised when a movement speed is invalid, usually negative or over a limit"""

    def __init__(self, msg):
        self.message = msg
