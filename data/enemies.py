from pygame import image
from scripts.enemies.enemy_type import EnemyType
from data.items import *

ENEMY_EXAMPLE = EnemyType(
  width = 64,
  height = 64,
  damage = 2,
  attack_cooldown = 400,
  knockback_intensity = 0.3,
  health = 5,
  speed = 0.05,
  drops = [
    [COMPASS, 15],
    [PINK_ROSE, 15],
    [HONEY, 15],
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
  run_duration = 1200,
  drops = [
    [TEDDY_BEAR, 10],
    [TRUMPET, 15],
    [EGGS, 20],
  ],
)

ENEMY_EXAMPLE_3 = EnemyType(
  spritesheet = image.load("placeholder/graphics/enemies/evil_enemy.png"),
  number_of_frames = 3,
  width = 32,
  height = 32,
  damage = 0,
  attack_cooldown = 200,
  knockback_intensity = 1,
  health = 1,
  speed = 0.2,
  run_duration = 600,
  drops = [
    [FEATHER, 10],
    [CHEESE, 10],
    [EGGS, 15],
  ],
)

ENEMY_EXAMPLE_4 = EnemyType(
  spritesheet = image.load("placeholder/graphics/enemies/enemy.png"),
  number_of_frames = 3,
  sprite_y_offset = 16,
  width = 32,
  height = 32,
  damage = 1,
  attack_cooldown = 300,
  knockback_intensity = 0.15,
  health = 3,
  speed = 0.07,
  drops = [
    [TOOTH, 10],
    [BELT, 15],
    [EGGS, 20],
  ],
)

enemy_types_list = [
  ENEMY_EXAMPLE,
  ENEMY_EXAMPLE_2,
  ENEMY_EXAMPLE_3,
  ENEMY_EXAMPLE_4,
]
