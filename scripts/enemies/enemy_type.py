from pygame import Surface

class EnemyType:
  def __init__(self, width: int, height: int, health: int, damage: int, attack_cooldown: int, knockback_intensity: float, speed: float, drops: list[list], spritesheet: Surface, number_of_frames: int, run_duration = 0, sprite_x_offset = 0, sprite_y_offset = 0) -> None:
    self.health = health
    self.damage = damage
    self.attack_cooldown = attack_cooldown
    self.knockback_intensity = knockback_intensity
    self.speed = speed
    self.run_duration = run_duration
    self.width = width
    self.height = height
    # drops são uma lista no formato: [[tipo_de_item1, chance1], [tipo_de_item2, chance2]]
    # (chance é um int entre 0 e 100 e tipo_de_item é um ItemType)
    self.drops = drops
    self.spritesheet = spritesheet
    self.number_of_frames = number_of_frames
    self.sprite_x_offset = sprite_x_offset
    self.sprite_y_offset = sprite_y_offset
