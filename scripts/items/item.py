from pygame import Surface
from scripts.items.item_type import ItemType
from scripts.entity import Entity

class Item(Entity):
  def __init__(self, item_type: ItemType, x: float, y: float) -> None:
    super().__init__(
      x = x,
      y = y,
      width = 32,
      height = 32,
    )
    self.item_type = item_type

  def draw(self, screen: Surface):
    screen.blit(
      source = self.item_type.image,
      dest = (self.x, self.y),
    )

  def apply_effect(self, player):
    self.item_type.effect(player)
