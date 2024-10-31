"""Defines the class position handler with static methods to check
    whether or not positions are inside the map boundaries
"""

import settings

class PositionHandler:
    """Class that handles positions and boundaries within the map"""

    @staticmethod
    def is_position_within_boundaries(position):
        """Whether or not the position is inside the map
        
            Args:
                Position (Vector2): the position to check
        """

        return (
            settings.TILE_WIDTH <= position.x <= settings.WORLD_LIMIT_WIDTH and settings.TILE_HEIGHT <= position.y <= settings.WORLD_LIMIT_HEIGHT
        )
