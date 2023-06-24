import pygame
from scripts.player.weapon.weapon_type import WeaponType
from scripts.player.weapon.melee_weapon import MeleeWeapon
from data.directions import Directions

class Weapon:
  def __init__(self, type: WeaponType) -> None:
    self.type = type

    self.x = 0
    self.y = 0

  def draw(self, screen: pygame.Surface):
    screen.blit(
      source = self.type.attack_animation,
      dest = (self.x, self.y),
      # area = , TODO adicionar animações
    )

  def update(self, enemies: list, x: float, y: float, direction: Directions):
    self.x = x
    self.y = y

    if type(self.type) == MeleeWeapon:
      self.__swing(direction, enemies)

  def __swing(self, direction: Directions, enemies: list):
    if type(self.type) != MeleeWeapon:
      raise Exception("This instance of Weapon cannot swing. Only a WeaponType of MeleeWeapon can swing.")

    # Inversão de width e height se estiver olhando para os lados
    width = self.type.hitbox_width if (direction == Directions.UP or direction == Directions.DOWN) else self.type.hitbox_height
    height = self.type.hitbox_height if (direction == Directions.UP or direction == Directions.DOWN) else self.type.hitbox_width

    # Divisão da colisão da lâmina igualmente para os dois lados
    if direction == Directions.UP or direction == Directions.DOWN:
      self.x -= width / 2 - 16
    elif direction == Directions.LEFT or direction == Directions.RIGHT:
      self.y -= height / 2 - 16

    hitbox = pygame.Rect(self.x, self.y, width, height)

    for enemy in enemies:
      if hitbox.colliderect(enemy.collider):
        enemy.take_damage(
          damage = self.type.damage,
          direction = direction,
          knockback_intensity = self.type.knockback_intensity,
        )
