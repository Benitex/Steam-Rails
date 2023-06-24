from scripts.entity import Entity
from scripts.player.player import Player

class Door(Entity):
  def __init__(self, is_open = False) -> None:
    super().__init__(
      x = 512,
      y = 160,
      width = 32,
      height = 64,
    )
    self.is_open = is_open

  def should_change_room(self, players: list[Player]) -> bool:
    for player in players:
      if self.is_open and self.is_colliding_with(player):
        return True
    return False
