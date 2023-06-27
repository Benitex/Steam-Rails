import pygame

class PlayerControls:
  def __init__(self, up: int, down: int, left: int, right: int, action: int, attack: int, dodge: int) -> None:
    self.UP = up
    self.DOWN = down
    self.LEFT = left
    self.RIGHT = right
    self.ACTION = action
    self.ATTACK = attack
    self.DODGE = dodge

  UP = pygame.K_UP
  DOWN = pygame.K_DOWN
  LEFT = pygame.K_LEFT
  RIGHT = pygame.K_RIGHT
  ACTION = pygame.K_SPACE
  ATTACK = pygame.K_SPACE
  DODGE = pygame.K_LSHIFT

  def is_any_key_in_controls_pressed(self, keys_pressed: pygame.key.ScancodeWrapper):
    return keys_pressed[self.UP] or keys_pressed[self.DOWN] or keys_pressed[self.LEFT] or keys_pressed[self.RIGHT] or keys_pressed[self.ACTION] or keys_pressed[self.ATTACK] or keys_pressed[self.DODGE]
