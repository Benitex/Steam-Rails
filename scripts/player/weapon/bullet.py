import pygame
from scripts.entity import Entity
from data.directions import Directions

class Bullet(Entity):
  def __init__(self, sprite: pygame.Surface, x: float, y: float, width: int, height: int, speed: float, direction: Directions) -> None:
    super().__init__(x, y, width, height)
    self.sprite = sprite
    self.speed = speed
    self.direction = direction

  def draw(self, screen: pygame.Surface):
    screen.blit(
      source = self.sprite,
      dest = (self.x, self.y),
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

    self.collider = pygame.Rect(
      (self.x, self.y),
      (self.width, self.height),
    )
