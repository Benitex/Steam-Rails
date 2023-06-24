from pygame import image
from scripts.items.item_type import ItemType
from scripts.player.player import Player

def example_effect(player: Player):
  player.speed *= 10
ITEM_EXAMPLE = ItemType(
  effect = lambda player : example_effect(player),
  image = image.load("placeholder/graphics/item.png"),
)

def modify_max_health(player: Player, amount: int):
  player.max_health += amount
  player.health += amount
HEALTH_EXTENDER_EXAMPLE = ItemType(
  effect = lambda player : modify_max_health(player, 1),
  image = image.load("placeholder/graphics/potion.png"),
)
