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

  def is_colliding_with(self, entity):
    return self.collider.colliderect(entity.collider)

  def get_distance_to(self, entity):
    return hypot(self.x - entity.x, self.y - entity.y)

  def get_center_coordinate(self):
    return self.x - self.width/2, self.y - self.height/2

  def draw_collider(self, screen: pygame.Surface):
    pygame.draw.rect(screen, "red", self.collider)
