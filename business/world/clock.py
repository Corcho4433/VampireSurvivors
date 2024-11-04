"""A singleton clock that can be called by all business classes and keeps
    a constant track of the game's time
"""


from settings import FPS
from business.world.interfaces import IClock

class Clock(IClock):
    """A clock that counts time in the world"""

    __active_clock = None

    def __new__(cls):
        if cls.__active_clock is None:
            cls.__active_clock = super().__new__(cls)
            cls.__active_clock.__clock_time = 0 #pylint: disable=W0212
        return cls.__active_clock

    def count(self):
        self.__clock_time += 1 / FPS

    def set_time(self, new_time: int):
        self.__clock_time = new_time #pylint: disable=W0201

    @property
    def time(self):
        return self.__clock_time
