from pygame import Surface, mixer, transform

class WeaponType:
  def __init__(
    self,
    is_melee: bool,
    icon: Surface,
    attack_animation: Surface,
    sound_effect: mixer.Sound,
    damage: int, attack_duration: int,
    knockback_intensity: float,
    hitbox_width: int,
    hitbox_height: int,
    bullet_speed = 0.0,
    number_of_frames = 4,
    scale = 2,
  ) -> None:
    self.is_melee = is_melee
    self.icon = transform.scale_by(icon, scale).convert_alpha()
    self.attack_animation = transform.scale_by(attack_animation, scale).convert_alpha()
    self.number_of_frames = number_of_frames
    self.sound_effect = sound_effect
    self.bullet_speed = bullet_speed * scale
    self.damage = damage
    self.attack_duration = attack_duration
    self.knockback_intensity = knockback_intensity * scale
    self.hitbox_width = hitbox_width * scale
    self.hitbox_height = hitbox_height * scale
