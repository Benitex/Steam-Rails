import pygame
from map.tileset import Tileset
from enemies.enemy import Enemy

class Room:
  def __init__(self, tile_layers_files: list, enemies = [], items = [], chests = []) -> None:
    self.tile_layers = [
      self.__convert_CSV_to_map_layer(file) for file in tile_layers_files
    ]
    self.enemies = enemies
    self.items = items
    self.chests = chests

    # TODO gerar obstáculos e modificações na sala

    if len(enemies) == 0:
      # TODO gerar inimigos aleatoriamente
      enemies.append(Enemy(
        spritesheet = pygame.image.load("placeholder/graphics/enemy.png"),
        x = 150, y = 150,
        speed = 0.1,
        damage = 1,
        health = 2,
      ))

  TILESET = Tileset(
    image = pygame.image.load("placeholder/graphics/tileset.png"), # TODO adicionar o tileset real
    tile_size = 32,
    tiles_in_a_row = 10,
    collisionable_tiles = [],
  )
  MAP_WIDTH = 19 # quantidade de tiles em uma linha do mapa

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

