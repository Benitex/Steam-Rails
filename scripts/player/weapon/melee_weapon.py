import pygame
from scripts.player.weapon.weapon import Weapon
from scripts.player.weapon.weapon_type import WeaponType
from data.directions import Directions

class MeleeWeapon(Weapon):
  def __init__(self, type: WeaponType) -> None:
    super().__init__(type)

  def update(self, player_attack: int, enemies: list, x: float, y: float, direction: Directions):
    self.x = x
    self.y = y

    self.__attack(player_attack, direction, enemies)

  def __attack(self, player_attack: int, direction: Directions, enemies: list):
    # Inversão de width e height se estiver olhando para os lados
    width = self.type.hitbox_width if (direction == Directions.UP or direction == Directions.DOWN) else self.type.hitbox_height
    height = self.type.hitbox_height if (direction == Directions.UP or direction == Directions.DOWN) else self.type.hitbox_width

    # Posicionamento da arma
    match direction:
      case Directions.UP: self.y -= height
      case Directions.DOWN: self.y += 32
      case Directions.LEFT: self.x -= width
      case Directions.RIGHT: self.x += 32

    # Divisão da colisão da lâmina igualmente para os dois lados
    if direction == Directions.UP or direction == Directions.DOWN:
      self.x -= width / 2 - 16
    elif direction == Directions.LEFT or direction == Directions.RIGHT:
      self.y -= height / 2 - 16

    hitbox = pygame.Rect(self.x, self.y, width, height)

    for enemy in enemies:
      if hitbox.colliderect(enemy.collider):
        enemy.take_damage(
          damage = self.type.damage * player_attack,
          direction = direction,
          knockback_intensity = self.type.knockback_intensity,
        )
