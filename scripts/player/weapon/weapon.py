from abc import abstractmethod
import pygame
from scripts.player.weapon.weapon_type import WeaponType
from scripts.entity import Entity
from data.directions import Directions

class Weapon:
  def __init__(self, type: WeaponType) -> None:
    self.type = type

  x, y = 0, 0
  direction = Directions.UP

  @abstractmethod
  def draw(self, screen: pygame.Surface): pass

  @abstractmethod
  def update(self, dt: int, player_attack: int, entities: list[Entity]): pass

  def start_attack(self, x: float, y: float, direction: Directions):
    pygame.mixer.Sound.play(self.type.sound_effect)
    self.x = x
    self.y = y
    self.direction = direction
