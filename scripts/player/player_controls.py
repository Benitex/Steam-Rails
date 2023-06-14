import pygame

class PlayerControls:
  def __init__(self, up: int, down: int, left: int, right: int, attack: int, dodge: int) -> None:
    self.UP = up
    self.DOWN = down
    self.LEFT = left
    self.RIGHT = right
    self.ATTACK = attack
    self.DODGE = dodge

  UP = pygame.K_UP
  DOWN = pygame.K_DOWN
  LEFT = pygame.K_LEFT
  RIGHT = pygame.K_RIGHT
  ATTACK = pygame.K_SPACE
  DODGE = pygame.K_LSHIFT
