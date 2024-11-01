"""This module contains the Monster class, which represents a monster entity in the game."""

from pygame import Vector2

from business.entities.entity import MovableEntity
from business.entities.interfaces import IDamageable, IMonster
from business.handlers.cooldown_handler import CooldownHandler
from business.world.interfaces import IGameWorld
from business.handlers.collision_handler import CollisionHandler
from presentation.sprite import Sprite

class Monster(MovableEntity, IMonster):
    """A monster entity in the game."""

    def __init__(self, pos: Vector2, sprite: Sprite, mov_speed: int):
        super().__init__(pos, mov_speed, sprite)
        self.__health: int = 10
        self.__damage = 10
        self.__attack_range = 50
        self.__attack_cooldown = CooldownHandler(0.5)
        self._logger.debug("Created %s", self)

    def attack(self, target: IDamageable):
        """Attacks the target."""
        if not self.__attack_cooldown.is_action_ready():
            return

        if self._get_distance_to(target) < self.__attack_range:
            target.take_damage(self.damage)
            self.__attack_cooldown.put_on_cooldown()

    def __get_direction_towards_the_player(self, world: IGameWorld):
        direction: Vector2 = self.pos - world.player.pos
        y = direction.y * world.simulation_speed
        x = direction.x * world.simulation_speed

        if x != 0:
            x = -x // abs(x)

        if y != 0:
            y = -y // abs(y)

        return Vector2(x, y)

    #def __movement_collides_with_entities(
    #    self, dx: float, dy: float, entities: List[IHasSprite]
    #) -> bool:
    #    new_position = self.sprite.rect.move(dx, dy).inflate(-10, -10)
    #    return any(e.sprite.rect.colliderect(new_position) for e in entities)

    def update(self, world: IGameWorld):
        direction = self.__get_direction_towards_the_player(world)
        if direction.magnitude == 0:
            return

        colliding_pairs = CollisionHandler.get_monster_colliding_pairs(world)
        colliding_monsters = [monster for pair in colliding_pairs for monster in pair]

        if not self in colliding_monsters:
            self.move(direction)
        elif self in colliding_monsters:
            for monster, other in colliding_pairs:
                if monster == self or other == self:
                    monster = min(
                        [monster, other],
                        key=lambda monster: (monster.pos.distance_to(other.pos)),
                    )

                    monster.move(direction)


        self.attack(world.player)

        super().update(world)

    def __str__(self):
        return f"Monster(hp={self.health}, pos={self.pos.x, self.pos.y})"

    @property
    def damage(self):
        return self.__damage

    @property
    def health(self) -> int:
        return self.__health

    def take_damage(self, amount):
        self.__health = max(0, self.__health - abs(amount))
        self.sprite.take_damage()
