from pygame import image
from scripts.items.item_type import ItemType
from scripts.player.player import Player

def example_effect(player: Player):
  player.speed *= 10
ITEM_EXAMPLE = ItemType(
  effect = lambda player : example_effect(player),
  image = image.load("placeholder/graphics/item.png"),
)
