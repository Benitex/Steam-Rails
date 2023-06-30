from pygame import image
from scripts.items.item_type import ItemType
from data.item_effects import *

HEALTH_EXTENDER_EXAMPLE = ItemType(
  effect = lambda player : modify_max_health(player, 2),
  image = image.load("placeholder/graphics/items/potion.png"),
)
HEALING_POTION = ItemType(
  effect = lambda player : heal(player, 1),
  image = image.load("placeholder/graphics/items/healing.png"),
)
GREATER_HEALING_POTION = ItemType(
  effect = lambda player : heal(player, 2),
  image = image.load("placeholder/graphics/items/healing.png"),
)

STRENGTH_POTION = ItemType(
  effect = lambda player : modify_attack(player, 1),
  image = image.load("placeholder/graphics/items/item.png"),
)
WEAKNESS_POTION = ItemType(
  effect = lambda player : modify_attack(player, -1),
  image = image.load("placeholder/graphics/items/item.png"),
)

SPEED_POTION = ItemType(
  effect = lambda player : modify_speed(player, 1.3),
  image = image.load("placeholder/graphics/items/healing.png"),
)
TURTLE_POTION = ItemType(
  effect = lambda player : modify_speed(player, 0.8),
  image = image.load("placeholder/graphics/items/healing.png"),
)

FLOATING_POTION = ItemType(
  effect = lambda player : modify_knockback_duration(player, 100),
  image = image.load("placeholder/graphics/items/healing.png"),
)
ENDURANCE_POTION = ItemType(
  effect = lambda player : modify_knockback_duration(player, -100),
  image = image.load("placeholder/graphics/items/healing.png"),
)

DANCING_POTION = ItemType(
  effect = lambda player : modify_dodge_speed_multiplier(player, 0.5),
  image = image.load("placeholder/graphics/items/healing.png"),
)
STONE_POTION = ItemType(
  effect = lambda player : modify_dodge_speed_multiplier(player, -0.5),
  image = image.load("placeholder/graphics/items/healing.png"),
)
