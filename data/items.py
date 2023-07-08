from pygame import image
from scripts.items.item_type import ItemType
from scripts.items.item_effects import *

PINK_ROSE = ItemType(
  effect = lambda player : modify_max_health(player, 1.2),
  image = image.load("graphics/items/pink_rose.png"),
)
EGGS = ItemType(
  effect = lambda player : heal(player, 0.1),
  image = image.load("graphics/items/eggs.png"),
)
HONEY = ItemType(
  effect = lambda player : heal(player, 0.3),
  image = image.load("graphics/items/honey.png"),
)

TOOTH = ItemType(
  effect = lambda player : modify_attack(player, 1),
  image = image.load("graphics/items/tooth.png"),
)
TEDDY_BEAR = ItemType(
  effect = lambda player : modify_attack(player, -1),
  image = image.load("graphics/items/teddy_bear.png"),
)

TRUMPET = ItemType(
  effect = lambda player : modify_speed(player, 1.3),
  image = image.load("graphics/items/trumpet.png"),
)
ROOTS = ItemType(
  effect = lambda player : modify_speed(player, 0.8),
  image = image.load("graphics/items/roots.png"),
)

FEATHER = ItemType(
  effect = lambda player : modify_knockback_duration(player, 100),
  image = image.load("graphics/items/feather.png"),
)
BELT = ItemType(
  effect = lambda player : modify_knockback_duration(player, -100),
  image = image.load("graphics/items/belt.png"),
)

COMPASS = ItemType(
  effect = lambda player : modify_dodge_speed_multiplier(player, 0.5),
  image = image.load("graphics/items/compass.png"),
)
CHEESE = ItemType(
  effect = lambda player : modify_dodge_speed_multiplier(player, -0.5),
  image = image.load("graphics/items/cheese.png"),
)
