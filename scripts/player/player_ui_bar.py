import pygame
from scripts.player.player import Player
from scripts.player.weapon.weapon import Weapon

class PlayerUIBar:
  def __init__(self, player: Player, x: float, y: float) -> None:
    self.player = player
    self.x = x
    self.y = y

  def draw(self, screen: pygame.Surface, font: pygame.font.Font):
    self.__draw_player_sprite(screen)
    self.__draw_weapon_icon(screen)
    self.__draw_health_bar(screen, font)

  def __draw_player_sprite(self, screen: pygame.Surface):
    screen.blit(
      source = self.player.spritesheet,
      dest = (self.x + 10, self.y - 22),
      area = (0, 0, self.player.width, self.player.height * 2),
    )

  def __draw_weapon_icon(self, screen: pygame.Surface):
    if isinstance(self.player.weapon, Weapon):
      screen.blit(
        source = self.player.weapon.type.icon,
        dest = (self.x + 10, self.y + 42),
      )

  def __draw_health_bar(self, screen: pygame.Surface, font: pygame.font.Font):
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

    screen.blit(
      source = font.render(f"{self.player.health} / {self.player.max_health}", False, "white"),
      dest = (self.x + 58, self.y + 24),
    )
