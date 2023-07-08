from pygame import Surface
from scripts.items.item_type import ItemType
from scripts.entity import Entity

class Item(Entity):
  def __init__(self, item_type: ItemType, x: float, y: float, is_picked_up = False, scale = 2) -> None:
    super().__init__(
      x = x / scale,
      y = y / scale,
      width = 32,
      height = 32,
      scale = scale,
    )
    self.item_type = item_type
    self.is_picked_up = is_picked_up

  def draw(self, screen: Surface):
    screen.blit(
      source = self.item_type.image,
      dest = (self.x, self.y),
    )

  def apply_effect(self, player):
    self.item_type.effect(player)
