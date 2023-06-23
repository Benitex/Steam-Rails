from abc import abstractmethod
import pygame
from scripts.entity import Entity
from data.directions import Directions

class Character(Entity):
  def __init__(self, spritesheet: pygame.Surface, x: float, y: float, width: int, height: int, direction: Directions, health: int, speed: float) -> None:
    super().__init__(x, y, width, height)

    self.spritesheet = spritesheet
    self.direction = direction
    self.health = health
    self.speed = speed

  KNOCKBACK_DURATION = 100
  knockback_timer = KNOCKBACK_DURATION
  knockback_direction = None
  knockback_intensity = 0

  def is_dead(self) -> bool: return self.health <= 0

  def is_taking_knockback(self) -> bool:
    return self.knockback_timer < self.KNOCKBACK_DURATION

  @abstractmethod
  def draw(self, screen: pygame.Surface): pass

  def take_damage(self, damage: int, direction: Directions, knockback_intensity: float):
    self.health -= damage
    self.knockback_timer = 0
    self.knockback_direction = direction
    self.knockback_intensity = knockback_intensity

  def take_knockback(self, dt: int):
    self.knockback_timer += dt

    if type(self.knockback_direction) != Directions or self.knockback_intensity <= 0:
      return

    if self.knockback_direction == Directions.DOWN:
      self.y += self.knockback_intensity * dt
    elif self.knockback_direction == Directions.LEFT:
      self.x -= self.knockback_intensity * dt
    elif self.knockback_direction == Directions.RIGHT:
      self.x += self.knockback_intensity * dt
    elif self.knockback_direction == Directions.UP:
      self.y -= self.knockback_intensity * dt
