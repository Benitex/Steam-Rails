import pygame
from scripts.player.player import Player
from scripts.player.weapon.weapon import Weapon

class PlayerUIBar:
  def __init__(self, player: Player, x: float, y: float) -> None:
    self.player = player
    self.x = x
    self.y = y

  def draw(self, screen: pygame.Surface):
    # TODO adicionar imagem de fundo
    self.__draw_weapon_icon(screen)
    self.__draw_health_bar(screen)

  def __draw_weapon_icon(self, screen: pygame.Surface):
    if type(self.player.weapon) == Weapon:
      screen.blit(
        source = self.player.weapon.type.icon,
        dest = (self.x + 10, self.y + 10),
      )

  def __draw_health_bar(self, screen: pygame.Surface):
    pygame.draw.rect(
      surface = screen,
      rect = pygame.Rect(
        self.x + 58,
        self.y,
        self.player.health * 100/self.player.max_health,
        16,
      ),
      color = (69, 194, 38),
    )
