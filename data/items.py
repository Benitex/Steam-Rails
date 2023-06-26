from pygame import image
from scripts.items.item_type import ItemType
from scripts.player.player import Player

def example_effect(player: Player):
  player.attack += 1
ITEM_EXAMPLE = ItemType(
  effect = lambda player : example_effect(player),
  image = image.load("placeholder/graphics/items/item.png"),
)

def modify_max_health(player: Player, amount: int):
  player.max_health += amount
  player.health += amount
HEALTH_EXTENDER_EXAMPLE = ItemType(
  effect = lambda player : modify_max_health(player, 1),
  image = image.load("placeholder/graphics/items/potion.png"),
)

def heal(player: Player, amount: int):
  player.health += amount
  if player.health > player.max_health:
    player.health = player.max_health
HEALING_POTION = ItemType(
  effect = lambda player : heal(player, 1),
  image = image.load("placeholder/graphics/items/healing.png"),
)
