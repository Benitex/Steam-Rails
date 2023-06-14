from pygame import Surface
from player.player_controls import PlayerControls

class Player:
  def __init__(self, controls: PlayerControls, spritesheet: Surface, x: int, y: int) -> None:
    self.controls = controls
    self.spritesheet = spritesheet

    self.x = x
    self.y = y

  x, y = 0, 0
  WIDTH, HEIGHT = 32, 32

  max_health = 5
  health = 5
  speed = 0.2

  def draw(self, screen: Surface):
    screen.blit(
      self.spritesheet,
      dest = (self.x, self.y),
      # area = (), TODO adicionar animações
    )

  def move(self, dt: int, keys_pressed):
    if keys_pressed[self.controls.UP]:
      self.y -= self.speed * dt
    elif keys_pressed[self.controls.DOWN]:
      self.y += self.speed * dt

    if keys_pressed[self.controls.RIGHT]:
      self.x += self.speed * dt
    elif keys_pressed[self.controls.LEFT]:
      self.x -= self.speed * dt

    if keys_pressed[self.controls.ATTACK]:
      self.__attack()

    if keys_pressed[self.controls.DODGE]:
      self.__dodge()

  def __attack(self):
    pass

  def __dodge(self):
    pass
