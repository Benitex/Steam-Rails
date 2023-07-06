from pygame import image
from scripts.enemies.enemy_type import EnemyType
from data.items import *

BAT = EnemyType(
  spritesheet = image.load("graphics/enemies/bat.png"),
  number_of_frames = 4,
  width = 16,
  height = 16,
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

RAT = EnemyType(
  spritesheet = image.load("graphics/enemies/rat.png"),
  number_of_frames = 6,
  width = 16,
  height = 16,
  damage = 1,
  attack_cooldown = 300,
  knockback_intensity = 0.15,
  health = 3,
  speed = 0.07,
  drops = [],
)

WOLF = EnemyType(
  spritesheet = image.load("graphics/enemies/wolf.png"),
  number_of_frames = 6,
  width = 48,
  height = 16,
  sprite_y_offset = 16,
  damage = 1,
  attack_cooldown = 300,
  knockback_intensity = 0.15,
  health = 3,
  speed = 0.2,
  run_duration = 1200,
  drops = [
    [TEDDY_BEAR, 10],
    [TRUMPET, 15],
    [EGGS, 20],
  ],
)

GOLEM = EnemyType(
  spritesheet = image.load("graphics/enemies/golem.png"),
  number_of_frames = 4,
  width = 32,
  height = 32,
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
  health = 1,
  speed = 0.2,
  run_duration = 600,
  drops = [
    [FEATHER, 10],
    [CHEESE, 10],
    [EGGS, 15],
  ],
)

enemy_types_list = [GOLEM, WOLF, SLIME, BAT, RAT]
