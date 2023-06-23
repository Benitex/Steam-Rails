from pygame import Surface
from scripts.entity import Entity
from scripts.player.weapon.weapon import Weapon
from scripts.player.weapon.weapon_type import WeaponType

class Chest(Entity):
  def __init__(self, sprite: Surface, weapon_type: WeaponType, x: float, y: float, is_infinite = False) -> None:
    super().__init__(
      x = x,
      y = y,
      width = 32,
      height = 32,
    )
    self.weapon_type = weapon_type
    self.sprite = sprite
    self.is_infinite = is_infinite

  def draw(self, screen: Surface):
    screen.blit(
      source = self.sprite,
      dest = (self.x, self.y),
    )
    screen.blit(
      source = self.weapon_type.icon,
      dest = (self.x, self.y - 32),
    )

  def change_weapons(self, player_weapon = None) -> Weapon:
    weapon = Weapon(self.weapon_type)

    if (not self.is_infinite) and type(player_weapon) == Weapon:
      self.weapon_type = player_weapon.type

    return weapon