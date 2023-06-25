from abc import abstractmethod
import pygame
from scripts.player.weapon.weapon_type import WeaponType
from data.directions import Directions

class Weapon:
  def __init__(self, type: WeaponType) -> None:
    self.type = type

  x, y = 0, 0

  def draw(self, screen: pygame.Surface):
    screen.blit(
      source = self.type.attack_animation,
      dest = (self.x, self.y),
      # area = , TODO adicionar animações
    )

  @abstractmethod
  def update(self, player_attack: int, enemies: list, x: float, y: float, direction: Directions): pass

  @abstractmethod
  def __attack(self, player_attack: int, direction: Directions, enemies: list): pass
