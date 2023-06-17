import pygame
from items.item_type import ItemType
from player.player import Player

class Item:
  def __init__(self, item_type: ItemType, x: int, y: int) -> None:
    self.item_type = item_type

    self.x = x
    self.y = y
    self.collider = pygame.Rect(
      (self.x, self.y),
      (self.WIDTH, self.HEIGHT),
    )

  WIDTH, HEIGHT = 32, 32

  def draw(self, screen: pygame.Surface):
    screen.blit(
      source = self.item_type.image,
      dest = (self.x, self.y),
    )

  def is_colliding_with(self, player: Player) -> bool:
    return self.collider.colliderect(player.collider)

  def apply_effect(self, player: Player):
    self.item_type.effect(player)
