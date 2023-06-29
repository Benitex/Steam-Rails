from pygame import image
from scripts.enemies.enemy_type import EnemyType
from data.items import *

ENEMY_EXAMPLE = EnemyType(
  width = 64,
  height = 64,
  damage = 1,
  attack_cooldown = 240,
  knockback_intensity = 0.3,
  health = 5,
  speed = 0.05,
  drops = [
    [HEALTH_EXTENDER_EXAMPLE, 10],
    [HEALING_POTION, 20]
  ],
  spritesheet = image.load("placeholder/graphics/enemies/Eyegore_Statue.png"),
  number_of_frames = 10,
  sprite_y_offset = 32,
)

ENEMY_EXAMPLE_2 = EnemyType(
  spritesheet = image.load("placeholder/graphics/enemies/snake.png"),
  number_of_frames = 4,
  width = 48,
  height = 32,
  damage = 1,
  attack_cooldown = 300,
  knockback_intensity = 0.2,
  health = 2,
  speed = 0.1,
  drops = [
    [ITEM_EXAMPLE, 10],
    [HEALING_POTION, 20],
  ],
)

enemy_types_list = [
  ENEMY_EXAMPLE,
  ENEMY_EXAMPLE_2,
]
