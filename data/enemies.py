from pygame import image
from scripts.enemies.enemy_type import EnemyType
from data.items import *

ENEMY_EXAMPLE = EnemyType(
  spritesheet = image.load("placeholder/graphics/enemy.png"),
  width = 32,
  height = 32,
  damage = 1,
  attack_cooldown = 240,
  knockback_intensity = 0.05,
  health = 3,
  speed = 0.05,
  drops = [
    [ITEM_EXAMPLE, 10],
  ],
)
ENEMY_EXAMPLE_2 = EnemyType(
  spritesheet = image.load("placeholder/graphics/enemy.png"),
  width = 32,
  height = 32,
  damage = 1,
  attack_cooldown = 300,
  knockback_intensity = 0.1,
  health = 1,
  speed = 0.1,
  drops = [
    [ITEM_EXAMPLE, 20],
  ],
)

enemy_types_list = [
  ENEMY_EXAMPLE,
  ENEMY_EXAMPLE_2,
]
