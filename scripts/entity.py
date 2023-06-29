import pygame
from math import hypot

class Entity:
  def __init__(self, x: float, y: float, width: int, height: int) -> None:
    self.x = x
    self.y = y
    self.width = width
    self.height = height

    self.collider = pygame.Rect(
      (self.x, self.y),
      (self.width, self.height),
    )

  def is_colliding_with(self, entity) -> bool:
    return self.collider.colliderect(entity.collider)

  def get_distance_to(self, entity) -> float:
    return hypot(self.x - entity.x, self.y - entity.y)

  def draw_collider(self, screen: pygame.Surface):
    pygame.draw.rect(screen, "red", self.collider)
