import pygame
from scripts.enemies.enemy_type import EnemyType
from scripts.entity import Entity
from scripts.player.player import Player

class Enemy(Entity):
  def __init__(self, enemy_type: EnemyType, x: float, y: float) -> None:
    super().__init__(
      x = x,
      y = y,
      width = enemy_type.width,
      height = enemy_type.height,
    )
    self.type = enemy_type

  chosen_player = None

  def update(self, dt: int, players: list[Player]):
    self.__choose_player(players)
    self.__move(dt)

    self.collider = pygame.Rect(
      (self.x, self.y),
      (self.type.width, self.type.height),
    )

  def draw(self, screen: pygame.Surface):
    screen.blit(
      source = self.type.spritesheet,
      dest = (self.x, self.y),
      # area = (), TODO adicionar animações
    )

  def __move(self, dt: int):
    if type(self.chosen_player) != Player: return

    normalizer = self.__movement_normalizer()
    # TODO parar o movimento se estiver muito perto do jogador

    if self.x < self.chosen_player.x:
      self.x += self.type.speed / normalizer * dt
    elif self.x > self.chosen_player.x:
      self.x -= self.type.speed / normalizer * dt

    if self.y < self.chosen_player.y:
      self.y += self.type.speed / normalizer * dt
    elif self.y > self.chosen_player.y:
      self.y -= self.type.speed / normalizer * dt

  def __movement_normalizer(self) -> float:
    if type(self.chosen_player) != Player: return 1

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
        if self.get_distance_to(player) < self.get_distance_to(self.chosen_player):
          self.chosen_player = player

  def __attack(self, player: Player):
    pass
