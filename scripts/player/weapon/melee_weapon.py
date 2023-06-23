from pygame import Surface
from scripts.player.weapon.weapon_type import WeaponType

class MeleeWeapon(WeaponType):
  def __init__(self, icon: Surface, attack_animation: Surface, damage: int, attack_duration: int, hitbox_width: int, hitbox_height: int) -> None:
    super().__init__(icon, attack_animation, damage, attack_duration)

    self.hitbox_width = hitbox_width
    self.hitbox_height = hitbox_height
