import pygame
from scripts.entity import Entity
from data.directions import Directions

class Bullet(Entity):
  def __init__(self, sprite: pygame.Surface, x: float, y: float, width: int, height: int, speed: float, direction: Directions, scale = 1) -> None:
    super().__init__(x, y, width, height, scale)
    self.sprite = sprite
    self.speed = speed
    self.direction = direction

  def draw(self, screen: pygame.Surface):
    y = 0
    match self.direction:
      case Directions.RIGHT:
        y = self.width
      case Directions.LEFT:
        y = self.height + self.width
      case Directions.UP:
        y = self.height + self.width * 2

    screen.blit(
      source = self.sprite,
      dest = (self.x, self.y),
      area = (0, y, self.width, self.height),
    )

  def update(self, dt):
    match self.direction:
      case Directions.UP:
        self.y -= self.speed * dt
      case Directions.DOWN:
        self.y += self.speed * dt
      case Directions.RIGHT:
        self.x += self.speed * dt
      case Directions.LEFT:
        self.x -= self.speed * dt

    self.collider.update(
      (self.x, self.y),
      (self.width, self.height),
    )
