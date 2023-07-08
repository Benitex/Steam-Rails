import pygame, random
from scripts.map.tileset import Tileset
from scripts.map.objects.door import Door
from scripts.map.objects.chest import Chest
from scripts.entity import Entity
from scripts.enemies.enemy import Enemy
from data.enemies import enemy_types_list
from data.weapons import weapons

class Room:
  def __init__(self, tile_layers_files: list, number_of_players: int, generate_enemies = True, enemy_difficulty_multiplier = 1, enemies = None, items = None, chests = None) -> None:
    self.tile_layers = [
      self.__convert_CSV_to_map_layer(file) for file in tile_layers_files
    ]
    self.walls = self.__get_colliders_from_tileset()
    self.enemies = enemies or []
    self.items = items or []
    self.chests = chests or []
    self.door = Door(
      sprite = self.DOOR_SPRITE,
      x = 672, y = 224,
    )

    if len(self.chests) == 0:
      if random.randint(1, 100) <= self.CHEST_SPAWN_RATE:
        for player_number in range(number_of_players):
          self.chests.append(Chest(
            sprite = self.CHEST_SPRITE,
            weapon_type = random.choice(weapons),
            x = 288 + player_number * 96,
            y = 160,
          ))

    if generate_enemies and len(self.enemies) == 0:
      number_of_enemies = 0
      for player in range(number_of_players):
        number_of_enemies += random.randint(3, 5)

      self.enemies += self.generate_enemies(number_of_enemies, enemy_difficulty_multiplier)

  TILESET = Tileset(
    image = pygame.transform.scale2x(pygame.image.load("graphics/tileset.png")).convert_alpha(),
    tile_size = 64,
    tiles_in_a_row = 9,
    collisionable_tiles = [
      0,
      31,
      40, 41,
      45, 47, 48, 49,
      54, 55, 56,
      63,
    ],
  )
  CHEST_SPRITE = TILESET.image.subsurface(
    pygame.Rect(
      (4 * TILESET.tile_size, 5 * TILESET.tile_size),
      (TILESET.tile_size, TILESET.tile_size),
    )
  )
  DOOR_SPRITE = TILESET.image.subsurface(
    pygame.Rect(
      (1 * TILESET.tile_size, 5 * TILESET.tile_size),
      (TILESET.tile_size, TILESET.tile_size * 3),
    )
  )
  MAP_WIDTH = 26 # quantidade de tiles em uma linha do mapa
  CHEST_SPAWN_RATE = 25

  def is_complete(self) -> bool:
    return len(self.enemies) == 0

  def get_entities(self) -> list[Entity]:
    return self.enemies + self.items + self.chests + self.walls + [self.door]

  def update(self):
    if self.is_complete():
      self.door.is_open = True
      for chest in self.chests:
        chest.is_open = True

  def draw(self, screen: pygame.Surface):
    for layer in self.tile_layers:
      for tile_number, tile in enumerate(layer):
        if tile == -1: continue

        screen.blit(
          source = self.TILESET.image,
          dest = (
            (tile_number % self.MAP_WIDTH) * self.TILESET.tile_size,
            (tile_number // self.MAP_WIDTH) * self.TILESET.tile_size,
          ),
          area = (
            (tile % self.TILESET.tiles_in_a_row) * self.TILESET.tile_size,
            (tile // self.TILESET.tiles_in_a_row) * self.TILESET.tile_size,
            self.TILESET.tile_size,
            self.TILESET.tile_size,
          ),
        )

    for chest in self.chests:
      chest.draw(screen)
    self.door.draw(screen)

  def __convert_CSV_to_map_layer(self, file) -> list[int]:
    layer = []
    for line in file.readlines():
      for tile in line.split(","):
        layer.append(int(tile))

    return layer

  def __get_colliders_from_tileset(self) -> list[Entity]:
    colliders = []

    for layer in self.tile_layers:
      for tile_number, tile in enumerate(layer):
        if self.TILESET.is_tile_collisionable(tile):
          tile = Entity(
            x = (tile_number % self.MAP_WIDTH) * self.TILESET.tile_size,
            y = (tile_number // self.MAP_WIDTH) * self.TILESET.tile_size,
            width = self.TILESET.tile_size,
            height = self.TILESET.tile_size,
            scale = 1,
          )
          if tile not in colliders: colliders.append(tile)

    return colliders

  def generate_enemies(self, number_of_enemies: int, difficulty_multiplier = 1) -> list[Enemy]:
    enemies = []
    for i in range(number_of_enemies):
      enemy_type = random.choice(enemy_types_list)
      enemies.append(Enemy(
        enemy_type = enemy_type,
        difficulty_multiplier = difficulty_multiplier,
        x = random.randint(9 * self.TILESET.tile_size, 18 * self.TILESET.tile_size - enemy_type.width),
        y = random.randint(5 * self.TILESET.tile_size, 10 * self.TILESET.tile_size - enemy_type.height),
      ))
    return enemies
