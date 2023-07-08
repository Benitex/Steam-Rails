from pygame import Surface, mixer
from scripts.entity import Entity
from scripts.player.weapon.weapon import Weapon
from scripts.player.weapon.weapon_type import WeaponType
from scripts.player.weapon.melee_weapon import MeleeWeapon
from scripts.player.weapon.ranged_weapon import RangedWeapon

class Chest(Entity):
  def __init__(self, sprite: Surface, weapon_type: WeaponType, x: float, y: float, is_open = False, is_infinite = False) -> None:
    super().__init__(
      x = x,
      y = y,
      width = 32,
      height = 32,
    )
    self.weapon_type = weapon_type
    self.sprite = sprite
    self.is_open = is_open
    self.is_infinite = is_infinite

  SOUND_EFFECT = mixer.Sound("audio/sound_effects/chest.wav")

  def draw(self, screen: Surface):
    screen.blit(
      source = self.sprite,
      dest = (self.x, self.y),
    )
    if self.is_open:
      screen.blit(
        source = self.weapon_type.icon,
        dest = (self.x, self.y - 32 * 2),
      )

  def change_weapons(self, player_weapon = None) -> Weapon:
    mixer.Sound.play(self.SOUND_EFFECT)
    weapon = MeleeWeapon(self.weapon_type) if (self.weapon_type.is_melee) else RangedWeapon(self.weapon_type)

    if (not self.is_infinite) and isinstance(player_weapon, Weapon):
      self.weapon_type = player_weapon.type

    return weapon
