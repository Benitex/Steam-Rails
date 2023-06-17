from pygame import image
from items.item_type import ItemType
from player.player import Player

def example_effect(player: Player):
  player.speed *= 10
item_example = ItemType(
  effect = lambda player : example_effect(player),
  image = image.load("placeholder/graphics/item.png"),
)
