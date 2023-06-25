from pygame import Surface

class WeaponType:
  def __init__(self, is_melee: bool, icon: Surface, attack_animation: Surface, damage: int, attack_duration: int, knockback_intensity: float, hitbox_width: int, hitbox_height: int, bullet_speed = 0.0) -> None:
    self.is_melee = is_melee
    self.icon = icon
    self.attack_animation = attack_animation
    self.bullet_speed = bullet_speed
    self.damage = damage
    self.attack_duration = attack_duration
    self.knockback_intensity = knockback_intensity
    self.hitbox_width = hitbox_width
    self.hitbox_height = hitbox_height
