from abc import abstractmethod
from pygame import Surface
from scripts.entity import Entity

class Character(Entity):
  def __init__(self, spritesheet: Surface, x: float, y: float, width: int, height: int, health: int, speed: float) -> None:
    super().__init__(x, y, width, height)

    self.spritesheet = spritesheet
    self.health = health
    self.speed = speed

  def is_dead(self) -> bool: return self.health <= 0

  @abstractmethod
  def draw(self, screen: Surface): pass

  def take_damage(self, damage: int):
    self.health -= damage
    # TODO adicionar knockback
