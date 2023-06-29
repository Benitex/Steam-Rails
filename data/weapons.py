from pygame import image, mixer
from scripts.player.weapon.weapon_type import WeaponType

SWORD = WeaponType(
  is_melee = True,
  icon = image.load("placeholder/graphics/icons/sword.png"),
  attack_animation = image.load("placeholder/graphics/item.png"),
  sound_effect = mixer.Sound("audio/sound_effects/weapons/sword.wav"),
  damage = 2,
  attack_duration = 300,
  knockback_intensity = 0.1,
  hitbox_width = 64,
  hitbox_height = 32,
)

GREAT_SWORD = WeaponType(
  is_melee = True,
  icon = image.load("placeholder/graphics/icons/great_sword.png"),
  attack_animation = image.load("placeholder/graphics/item.png"),
  sound_effect = mixer.Sound("audio/sound_effects/weapons/great_sword.wav"),
  damage = 3,
  attack_duration = 400,
  knockback_intensity = 0.3,
  hitbox_width = 64,
  hitbox_height = 48,
)

HAMMER = WeaponType(
  is_melee = True,
  icon = image.load("placeholder/graphics/icons/hammer.png"),
  attack_animation = image.load("placeholder/graphics/item.png"),
  sound_effect = mixer.Sound("audio/sound_effects/weapons/hammer.wav"),
  damage = 3,
  attack_duration = 400,
  knockback_intensity = 0.5,
  hitbox_width = 32,
  hitbox_height = 48,
)

LANCE = WeaponType(
  is_melee = True,
  icon = image.load("placeholder/graphics/icons/lance.png"),
  attack_animation = image.load("placeholder/graphics/item.png"),
  sound_effect = mixer.Sound("audio/sound_effects/weapons/lance.wav"),
  damage = 2,
  attack_duration = 400,
  knockback_intensity = 0.01,
  hitbox_width = 16,
  hitbox_height = 64,
)

DAGGER = WeaponType(
  is_melee = True,
  icon = image.load("placeholder/graphics/icons/dagger.png"),
  attack_animation = image.load("placeholder/graphics/item.png"),
  sound_effect = mixer.Sound("audio/sound_effects/weapons/dagger.wav"),
  damage = 1,
  attack_duration = 200,
  knockback_intensity = 0.01,
  hitbox_width = 16,
  hitbox_height = 32,
)

PISTOL = WeaponType(
  is_melee = False,
  icon = image.load("placeholder/graphics/icons/pistol.png"),
  attack_animation = image.load("placeholder/graphics/gun.png"),
  sound_effect = mixer.Sound("audio/sound_effects/weapons/pistol.wav"),
  damage = 1,
  bullet_speed = 0.5,
  attack_duration = 400,
  knockback_intensity = 0.01,
  hitbox_width = 16,
  hitbox_height = 16,
)

SHOTGUN = WeaponType(
  is_melee = False,
  icon = image.load("placeholder/graphics/icons/shotgun.png"),
  attack_animation = image.load("placeholder/graphics/gun.png"),
  sound_effect = mixer.Sound("audio/sound_effects/weapons/shotgun.wav"),
  damage = 2,
  bullet_speed = 0.2,
  attack_duration = 700,
  knockback_intensity = 0.3,
  hitbox_width = 64,
  hitbox_height = 16,
)

BOW = WeaponType(
  is_melee = False,
  icon = image.load("placeholder/graphics/icons/bow.png"),
  attack_animation = image.load("placeholder/graphics/gun.png"),
  sound_effect = mixer.Sound("audio/sound_effects/weapons/bow.wav"),
  damage = 2,
  bullet_speed = 0.2,
  attack_duration = 400,
  knockback_intensity = 0.1,
  hitbox_width = 32,
  hitbox_height = 32,
)

MACHINE_GUN = WeaponType(
  is_melee = False,
  icon = image.load("placeholder/graphics/icons/machine_gun.png"),
  attack_animation = image.load("placeholder/graphics/gun.png"),
  sound_effect = mixer.Sound("audio/sound_effects/weapons/machine_gun.wav"),
  damage = 1,
  bullet_speed = 1,
  attack_duration = 200,
  knockback_intensity = 0.01,
  hitbox_width = 16,
  hitbox_height = 16,
)

BAZOOKA = WeaponType(
  is_melee = False,
  icon = image.load("placeholder/graphics/icons/bazooka.png"),
  attack_animation = image.load("placeholder/graphics/gun.png"),
  sound_effect = mixer.Sound("audio/sound_effects/weapons/bazooka.wav"),
  damage = 3,
  bullet_speed = 0.2,
  attack_duration = 800,
  knockback_intensity = 0.7,
  hitbox_width = 64,
  hitbox_height = 64,
)

melee_weapons = [SWORD, GREAT_SWORD, HAMMER, LANCE, DAGGER]
ranged_weapons = [PISTOL, SHOTGUN, BOW, MACHINE_GUN, BAZOOKA]
weapons = melee_weapons + ranged_weapons
