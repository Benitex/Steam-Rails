from pygame import image
from scripts.player.weapon.weapon_type import WeaponType

WEAPON_EXAMPLE = WeaponType(
  is_melee = True,
  icon = image.load("placeholder/graphics/item.png"),
  attack_animation = image.load("placeholder/graphics/item.png"),
  damage = 1,
  attack_duration = 200,
  knockback_intensity = 0.1,
  hitbox_width = 64,
  hitbox_height = 32,
)

WEAPON_EXAMPLE_2 = WeaponType(
  is_melee = True,
  icon = image.load("placeholder/graphics/gun.png"),
  attack_animation = image.load("placeholder/graphics/gun.png"),
  damage = 1,
  attack_duration = 200,
  knockback_intensity = 0.01,
  hitbox_width = 64,
  hitbox_height = 32,
)

melee_weapons = [WEAPON_EXAMPLE]
ranged_weapons = [WEAPON_EXAMPLE_2]
weapons = melee_weapons + ranged_weapons
