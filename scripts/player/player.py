import pygame
from player.player_controls import PlayerControls

class Player:
  def __init__(self, controls: PlayerControls, spritesheet: pygame.Surface, x: int, y: int, items = []) -> None:
    self.controls = controls
    self.spritesheet = spritesheet

    self.x = x
    self.y = y

    self.items = items

  x, y = 0, 0
  WIDTH, HEIGHT = 32, 32

  collider = pygame.Rect(0, 0, 0, 0)

  items = []
  max_health = 5
  health = 5
  speed = 0.15

  def update(self, dt: int, keys_pressed):
    if keys_pressed[self.controls.DODGE]:
      self.__dodge()
    elif keys_pressed[self.controls.ATTACK]:
      self.__attack()
    else:
      self.move(dt, keys_pressed)

    self.collider = pygame.Rect(
      (self.x, self.y + self.HEIGHT),
      (self.WIDTH, self.HEIGHT),
    )

  def draw(self, screen: pygame.Surface):
    screen.blit(
      self.spritesheet,
      dest = (self.x, self.y),
      # area = (), TODO adicionar animações
    )

  def move(self, dt: int, keys_pressed):
    normalizer = self.__movement_normalizer(keys_pressed)
  
    if keys_pressed[self.controls.UP]:
      self.y -= self.speed / normalizer * dt
    elif keys_pressed[self.controls.DOWN]:
      self.y += self.speed / normalizer * dt

    if keys_pressed[self.controls.RIGHT]:
      self.x += self.speed / normalizer * dt
    elif keys_pressed[self.controls.LEFT]:
      self.x -= self.speed / normalizer * dt

  def __movement_normalizer(self, keys_pressed) -> float:
    if keys_pressed[self.controls.UP] and keys_pressed[self.controls.RIGHT]:
      return 1.4
    if keys_pressed[self.controls.UP] and keys_pressed[self.controls.LEFT]:
      return 1.4
    if keys_pressed[self.controls.DOWN] and keys_pressed[self.controls.LEFT]:
      return 1.4
    if keys_pressed[self.controls.DOWN] and keys_pressed[self.controls.RIGHT]:
      return 1.4
  
    return 1

  def __attack(self):
    pass # TODO implementar método

  def __dodge(self):
    pass # TODO implementar método
