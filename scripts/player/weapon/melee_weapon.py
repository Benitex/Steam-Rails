import pygame
from scripts.player.weapon.weapon import Weapon
from scripts.player.weapon.weapon_type import WeaponType
from scripts.entity import Entity
from scripts.enemies.enemy import Enemy
from data.directions import Directions

class MeleeWeapon(Weapon, Entity):
  def __init__(self, type: WeaponType) -> None:
    Weapon.__init__(self, type)
    Entity.__init__(self, 0, 0, 0, 0)

  def update(self, player_attack: int, entities: list[Entity]):
    for enemy in entities:
      if type(enemy) == Enemy and self.is_colliding_with(enemy):
        enemy.take_damage(
          damage = self.type.damage * player_attack,
          direction = self.direction,
          knockback_intensity = self.type.knockback_intensity,
        )

  def start_attack(self, x: float, y: float, direction: Directions):
    super().start_attack(x, y, direction)

    # Inversão de width e height se estiver olhando para os lados
    width = self.type.hitbox_width if (direction == Directions.UP or direction == Directions.DOWN) else self.type.hitbox_height
    height = self.type.hitbox_height if (direction == Directions.UP or direction == Directions.DOWN) else self.type.hitbox_width

    # Posicionamento da arma
    match direction:
      case Directions.UP: self.y -= height
      case Directions.LEFT: self.x -= width

    # Divisão da colisão da largura igualmente para os dois lados
    if direction == Directions.UP or direction == Directions.DOWN:
      self.x -= width / 2 - 16
    elif direction == Directions.LEFT or direction == Directions.RIGHT:
      self.y -= height / 2 - 16

    self.collider = pygame.Rect(self.x, self.y, width, height)
