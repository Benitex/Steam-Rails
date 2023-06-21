import pygame
import random
from scripts.map.tileset import Tileset
from scripts.entity import Entity
from scripts.enemies.enemy import Enemy
from data.enemies import enemy_types_list

class Room:
  def __init__(self, tile_layers_files: list, number_of_players: int, number_of_enemies = 3, enemies = [], items = [], chests = []) -> None:
    self.tile_layers = [
      self.__convert_CSV_to_map_layer(file) for file in tile_layers_files
    ]
    self.enemies = enemies
    self.items = items
    self.chests = chests

    # TODO gerar obstáculos e modificações na sala

    if len(chests) == 0:
      if random.randint(1, 100) <= self.CHEST_SPAWN_RATE:
        for player in range(number_of_players):
          pass # self.chests.append(Chest()) TODO adicionar os baús com armas aleatórias

    if len(enemies) == 0:
      for i in range(number_of_enemies):
        enemies.append(Enemy(
          enemy_type = random.choice(enemy_types_list),
          x = 150, y = 150, # TODO gerar o inimigo em um lugar aleatório
        ))

  TILESET = Tileset(
    image = pygame.image.load("placeholder/graphics/tileset.png"), # TODO adicionar o tileset real
    tile_size = 32,
    tiles_in_a_row = 10,
    collisionable_tiles = [],
  )
  MAP_WIDTH = 19 # quantidade de tiles em uma linha do mapa
  CHEST_SPAWN_RATE = 25

  enemies = []
  items = []
  chests = []

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

  def __convert_CSV_to_map_layer(self, file) -> list[int]:
    layer = []
    for line in file.readlines():
      for tile in line.split(","):
        layer.append(int(tile))

    return layer

  def get_entities(self) -> list[Entity]:
    return self.enemies + self.items + self.chests
  