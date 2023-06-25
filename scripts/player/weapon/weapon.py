from abc import abstractmethod
import pygame
from scripts.player.weapon.weapon_type import WeaponType
from scripts.entity import Entity
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
  def update(self, player_attack: int, entities: list[Entity], x: float, y: float, direction: Directions): pass
