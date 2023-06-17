import pygame
from sys import exit
from player.player import Player
from player.player_controls import PlayerControls
from map.rooms.initial_room import InitialRoom

pygame.init()
screen = pygame.display.set_mode((608, 352))
clock = pygame.time.Clock()

current_room = InitialRoom()
players = [
  Player(
    x = 0,
    y = 0,
    spritesheet = pygame.image.load("placeholder/graphics/player.png"), # TODO adicionar o sprite real
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
    spritesheet = pygame.image.load("placeholder/graphics/player.png"), # TODO adicionar o sprite real
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

  current_room.draw(screen)

  for item in current_room.items:
    item.draw(screen)

  for player in players:
    if player.health > 0:
      player.draw(screen)
  
  pygame.display.update()

def update():
  clock.tick(60)
  dt = clock.get_time()
  keys_pressed = pygame.key.get_pressed()

  for player in players:
    player.update(dt, keys_pressed)

    for item in current_room.items:
      if item.is_colliding_with(player):
        item.apply_effect(player)
        player.items.append(item)
        current_room.items.remove(item)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  update()
  draw(screen)
