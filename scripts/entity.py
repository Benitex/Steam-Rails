import pygame
from math import hypot

class Entity:
  def __init__(self, x: float, y: float, width: int, height: int, scale = 2) -> None:
    self.x = x * scale
    self.y = y * scale
    self.width = width * scale
    self.height = height * scale

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
