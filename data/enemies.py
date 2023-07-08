from pygame import image
from scripts.enemies.enemy_type import EnemyType
from data.items import *

BAT = EnemyType(
  spritesheet = image.load("graphics/enemies/bat.png"),
  number_of_frames = 4,
  width = 16,
  height = 16,
  damage = 10,
  attack_cooldown = 300,
  knockback_intensity = 0.15,
  health = 30,
  speed = 0.07,
  drops = [
    [EGGS, 15],
    [FEATHER, 10],
    [ROOTS, 10],
  ],
)

RAT = EnemyType(
  spritesheet = image.load("graphics/enemies/rat.png"),
  number_of_frames = 6,
  width = 16,
  height = 16,
  damage = 15,
  attack_cooldown = 300,
  knockback_intensity = 0.2,
  health = 15,
  speed = 0.15,
  run_duration = 1200,
  drops = [
    [EGGS, 15],
    [TRUMPET, 10],
    [CHEESE, 10],
  ],
)

SLIME = EnemyType(
  spritesheet = image.load("graphics/enemies/slime.png"),
  number_of_frames = 4,
  width = 32,
  height = 16,
  sprite_y_offset = 16,
  damage = 0,
  attack_cooldown = 200,
  knockback_intensity = 1,
  health = 10,
  speed = 0.2,
  run_duration = 600,
  drops = [
    [HONEY, 15],
    [PINK_ROSE, 10],
    [BELT, 10],
  ],
)

WOLF = EnemyType(
  spritesheet = image.load("graphics/enemies/wolf.png"),
  number_of_frames = 6,
  width = 48,
  height = 16,
  sprite_y_offset = 16,
  damage = 20,
  attack_cooldown = 300,
  knockback_intensity = 0.3,
  health = 45,
  speed = 0.13,
  run_duration = 1200,
  drops = [
    [HONEY, 20],
    [TOOTH, 10],
    [COMPASS, 10],
  ],
)

GOLEM = EnemyType(
  spritesheet = image.load("graphics/enemies/golem.png"),
  number_of_frames = 4,
  width = 32,
  height = 32,
  damage = 30,
  attack_cooldown = 400,
  knockback_intensity = 0.3,
  health = 70,
  speed = 0.05,
  drops = [
    [PINK_ROSE, 10],
    [HONEY, 10],
    [TEDDY_BEAR, 10],
  ],
)

enemy_types_list = [GOLEM, WOLF, SLIME, BAT, RAT]
