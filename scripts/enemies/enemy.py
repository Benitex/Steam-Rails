import pygame
from player.player import Player
from math import hypot

class Enemy:
  def __init__(self, spritesheet: pygame.Surface, x: int, y: int, speed: float, health: int, damage: int) -> None:
    self.spritesheet = spritesheet
    self.x = x
    self.y = y
    self.health = health
    self.damage = damage
    self.speed = speed
    # TODO adicionar drops

  x, y = 0, 0
  width, height = 32, 32

  collider = pygame.Rect(0, 0, 0, 0)
  chosen_player = Player

  def update(self, dt: int, players: list[Player]):
    self.__choose_player(players)
    self.__move(dt)

    self.collider = pygame.Rect(
      (self.x, self.y),
      (self.width, self.height),
    )

  def draw(self, screen: pygame.Surface):
    screen.blit(
      source = self.spritesheet,
      dest = (self.x, self.y),
      # area = (), TODO adicionar animações
    )

  def __move(self, dt: int):
    normalizer = self.__movement_normalizer()
    # TODO parar o movimento se estiver muito perto do jogador

    if self.x < self.chosen_player.x:
      self.x += self.speed / normalizer * dt
    elif self.x > self.chosen_player.x:
      self.x -= self.speed / normalizer * dt

    if self.y < self.chosen_player.y:
      self.y += self.speed / normalizer * dt
    elif self.y > self.chosen_player.y:
      self.y -= self.speed / normalizer * dt

  def __movement_normalizer(self) -> float:
    if self.y < self.chosen_player.y and self.x > self.chosen_player.x:
      return 1.4
    if self.y < self.chosen_player.y and self.x < self.chosen_player.x:
      return 1.4
    if self.y > self.chosen_player.y and self.x > self.chosen_player.x:
      return 1.4
    if self.y > self.chosen_player.y and self.x < self.chosen_player.x:
      return 1.4
  
    return 1

  def __choose_player(self, players: list[Player]):
    self.chosen_player = players[0]
    if len(players) > 1:
      for player in players[1:]:
        if hypot(self.x - player.x, self.y - player.y) < hypot(self.x - self.chosen_player.x, self.y - self.chosen_player.y):
          self.chosen_player = player

  def __attack(self, player: Player):
    pass
