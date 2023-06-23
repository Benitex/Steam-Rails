from pygame import Surface

class WeaponType:
  def __init__(self, icon: Surface, attack_animation: Surface, damage: int, attack_duration: int) -> None:
    self.icon = icon
    self.attack_animation = attack_animation
    self.damage = damage
    self.attack_duration = attack_duration
