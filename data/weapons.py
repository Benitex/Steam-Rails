from pygame import image
from scripts.player.weapon.melee_weapon import MeleeWeapon

WEAPON_EXAMPLE = MeleeWeapon(
  icon = image.load("placeholder/graphics/item.png"),
  attack_animation = image.load("placeholder/graphics/item.png"),
  damage = 1,
  attack_duration = 200,
  hitbox_width = 64,
  hitbox_height = 32,
)
