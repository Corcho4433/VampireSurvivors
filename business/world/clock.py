from settings import FPS
from business.world.interfaces import IClock

class Clock(IClock):
    """A clock that counts time in the world"""

    __active_clock = None

    def __new__(cls):
        if cls.__active_clock is None:
            cls.__active_clock = super().__new__(cls)
            cls.__active_clock.__clock_time = 0
        return cls.__active_clock

    def count(self):
        self.__clock_time += 1 / FPS

    @property
    def time(self):
        return self.__clock_time
