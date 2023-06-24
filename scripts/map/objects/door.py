from pygame import Surface
from scripts.entity import Entity
from scripts.player.player import Player

class Door(Entity):
  def __init__(self, sprite: Surface, x: float, y: float, is_open = False) -> None:
    super().__init__(
      x = x,
      y = y,
      width = 32,
      height = 64,
    )
    self.sprite = sprite
    self.is_open = is_open

  def draw(self, screen: Surface):
    if not self.is_open:
      screen.blit(
        source = self.sprite,
        dest = (self.x, self.y),
      )

  def should_change_room(self, players: list[Player]) -> bool:
    for player in players:
      if self.is_open and self.is_colliding_with(player):
        return True
    return False
