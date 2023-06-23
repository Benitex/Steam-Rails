import pygame
from scripts.player.weapon.weapon_type import WeaponType
from scripts.player.weapon.melee_weapon import MeleeWeapon

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

  def update(self, enemies: list, x: float, y: float):
    self.x = x
    self.y = y

    if type(self.type) == MeleeWeapon:
      self.__swing(enemies)

  def __swing(self, enemies: list):
    if type(self.type) != MeleeWeapon:
      raise Exception("This instance of Weapon cannot swing. Only a WeaponType of MeleeWeapon can swing.")

    hitbox = pygame.Rect(
      (self.x, self.y),
      (self.type.hitbox_width, self.type.hitbox_height),
    )

    # TODO dano nos inimigos
