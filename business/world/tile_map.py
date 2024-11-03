"""Module that contains the TileMap class."""

from random import randint
import settings
from business.world.interfaces import ITileMap


class TileMap(ITileMap):
    """Class that represents the tile map of the game world."""

    def __init__(self):
        self.map_data = self.__generate_tile_map()

    def __generate_tile_map(self):
        # Create a 2D array of tile indices
        tile_map = [[self.__random_tile() for _ in range(settings.WORLD_COLUMNS)] for _ in range(settings.WORLD_ROWS)]

        for x in range(settings.WORLD_ROWS):
            tile_map[x][0] = self.__random_border()
            tile_map[0][x] = self.__random_border()
            tile_map[settings.WORLD_COLUMNS - 1][x] = self.__random_border()
            tile_map[x][settings.WORLD_COLUMNS - 1] = self.__random_border()

        return tile_map

    def get(self, row, col) -> int:
        # Get the tile index at a specific row and column
        return self.map_data[row][col]

    def __random_tile(self):
        return randint(0, 48)

    def __random_border(self):
        return randint(129, 130) + round(randint(0, 1)) * 16