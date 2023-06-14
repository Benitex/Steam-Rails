import pygame
from sys import exit
from player.player import Player
from player.player_controls import PlayerControls

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

players = [
  Player(
    x = 0,
    y = 0,
    spritesheet = pygame.image.load("graphics/placeholder/player.png"), # TODO adicionar o sprite real
    controls = PlayerControls(
      up = pygame.K_UP,
      down = pygame.K_DOWN,
      left = pygame.K_LEFT,
      right = pygame.K_RIGHT,
      attack = pygame.K_SPACE,
      dodge = pygame.K_LSHIFT,
    ),
  ),
  Player(
    x = 100,
    y = 0,
    spritesheet = pygame.image.load("graphics/placeholder/player.png"), # TODO adicionar o sprite real
    controls = PlayerControls(
      up = pygame.K_w,
      down = pygame.K_s,
      left = pygame.K_a,
      right = pygame.K_d,
      attack = pygame.K_SPACE,
      dodge = pygame.K_LSHIFT,
    ),
  ),
]

def draw(screen: pygame.Surface):
  screen.fill("black")

  for player in players:
    if player.health > 0:
      player.draw(screen)
  
  pygame.display.update()

def update():
  clock.tick(60)
  dt = clock.get_time()
  keys_pressed = pygame.key.get_pressed()

  for player in players:
    player.move(dt, keys_pressed)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  update()
  draw(screen)
