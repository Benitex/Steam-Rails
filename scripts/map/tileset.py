from pygame import Surface

class Tileset:
  def __init__(self, image: Surface, tile_size: int, tiles_in_a_row: int, collisionable_tiles: list[int]) -> None:
    self.image = image
    self.tile_size = tile_size
    self.tiles_in_a_row = tiles_in_a_row
    self.collisionable_tiles = collisionable_tiles

  def is_tile_collisionable(self, tile_number: int) -> bool:
    return tile_number in self.collisionable_tiles
