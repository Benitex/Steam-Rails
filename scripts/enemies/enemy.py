import pygame
from scripts.enemies.enemy_type import EnemyType
from scripts.character import Character
from scripts.player.player import Player
from data.directions import Directions

class Enemy(Character):
  def __init__(self, enemy_type: EnemyType, x: float, y: float) -> None:
    super().__init__(
      x = x,
      y = y,
      width = enemy_type.width,
      height = enemy_type.height,
      direction = Directions.DOWN,
      spritesheet = enemy_type.spritesheet,
      health = enemy_type.health,
      speed = enemy_type.speed,
    )
    self.type = enemy_type
    self.attack_timer = self.type.attack_cooldown

  chosen_player = None

  def update(self, dt: int, players: list[Player]):
    if self.is_taking_knockback():
      self.take_knockback(dt)

    if self.attack_timer > 0:
      self.attack_timer -= dt
      return

    self.__choose_player(players)
    self.__move(dt)

    self.collider = pygame.Rect(
      (self.x, self.y),
      (self.type.width, self.type.height),
    )

    for player in players:
      if self.is_colliding_with(player):
        self.__attack(player)

  def draw(self, screen: pygame.Surface):
    screen.blit(
      source = self.type.spritesheet,
      dest = (self.x, self.y),
      # area = (), TODO adicionar animações
    )

  def __move(self, dt: int):
    if type(self.chosen_player) != Player: return

    normalizer = self.__movement_normalizer()

    # FIXME corrigir direção do knockback
    if self.y < self.chosen_player.collider.y:
      self.direction = Directions.DOWN
      self.y += self.type.speed / normalizer * dt
    elif self.y > self.chosen_player.collider.y:
      self.direction = Directions.UP
      self.y -= self.type.speed / normalizer * dt

    if self.x < self.chosen_player.collider.x:
      self.direction = Directions.RIGHT
      self.x += self.type.speed / normalizer * dt
    elif self.x > self.chosen_player.collider.x:
      self.direction = Directions.LEFT
      self.x -= self.type.speed / normalizer * dt

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
    self.chosen_player = None
    if len(players) > 0:
      self.chosen_player = players[0]
      for player in players[1:]:
        if self.get_distance_to(player) < self.get_distance_to(self.chosen_player):
          self.chosen_player = player

  def __attack(self, player: Player):
    player.take_damage(
      damage = self.type.damage,
      direction = self.direction,
      knockback_intensity = 0.2,
    )
    self.attack_timer = self.type.attack_cooldown
