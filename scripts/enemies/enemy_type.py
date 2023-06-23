from pygame import Surface

class EnemyType:
  def __init__(self, spritesheet: Surface, width: int, height: int, health: int, damage: int, attack_cooldown: int, knockback_intensity: float, speed: float, drops: list[list]) -> None:
    self.spritesheet = spritesheet
    self.health = health
    self.damage = damage
    self.attack_cooldown = attack_cooldown
    self.knockback_intensity = knockback_intensity
    self.speed = speed
    self.width = width
    self.height = height
    # drops são uma lista no formato: [[tipo_de_item1, chance1], [tipo_de_item2, chance2]]
    # (chance é um int entre 0 e 100 e tipo_de_item é um ItemType)
    self.drops = drops
