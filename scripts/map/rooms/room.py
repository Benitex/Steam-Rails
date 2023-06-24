import pygame, random
from scripts.map.tileset import Tileset
from scripts.map.objects.door import Door
from scripts.map.objects.chest import Chest
from scripts.entity import Entity
from scripts.enemies.enemy import Enemy
from data.enemies import enemy_types_list
from data.weapons import weapons

class Room:
  def __init__(self, tile_layers_files: list, number_of_players: int, number_of_enemies = 3, enemies = None, items = None, chests = None) -> None:
    self.tile_layers = [
      self.__convert_CSV_to_map_layer(file) for file in tile_layers_files
    ]
    self.enemies = enemies or []
    self.items = items or []
    self.chests = chests or []
    self.door = Door()

    # TODO gerar obstáculos e modificações na sala

    if len(self.chests) == 0:
      if random.randint(1, 100) <= self.CHEST_SPAWN_RATE:
        for player_number in range(number_of_players):
          self.chests.append(Chest(
            sprite = self.CHEST_SPRITE,
            weapon_type = random.choice(weapons),
            x = 224 + player_number * 64, # TODO atualizar com a posição no mapa final
            y = 128,
          ))

    if len(self.enemies) == 0:
      for i in range(number_of_enemies):
        self.enemies.append(Enemy(
          enemy_type = random.choice(enemy_types_list),
          x = 150, y = 150, # TODO gerar o inimigo em um lugar aleatório
        ))

  TILESET = Tileset(
    image = pygame.image.load("placeholder/graphics/tileset.png"), # TODO adicionar o tileset real
    tile_size = 32,
    tiles_in_a_row = 10,
    collisionable_tiles = [],
  )
  CHEST_SPRITE = TILESET.image.subsurface(
    pygame.Rect(
      (0, 8 * TILESET.tile_size),
      (TILESET.tile_size, TILESET.tile_size),
    )
  )
  MAP_WIDTH = 19 # quantidade de tiles em uma linha do mapa
  CHEST_SPAWN_RATE = 25

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

  def __convert_CSV_to_map_layer(self, file) -> list[int]:
    layer = []
    for line in file.readlines():
      for tile in line.split(","):
        layer.append(int(tile))

    return layer

  def is_complete(self) -> bool:
    return len(self.enemies) == 0

  def get_entities(self) -> list[Entity]:
    return self.enemies + self.items + self.chests

  def move_entity_to_tile(self, entity: Entity, x: int, y: int):
    entity.x = x * self.TILESET.tile_size
    entity.y = y * self.TILESET.tile_size
