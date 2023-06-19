import pygame
from sys import exit
from map.rooms.initial_room import InitialRoom

pygame.init()
screen = pygame.display.set_mode((608, 384))
clock = pygame.time.Clock()

current_room = InitialRoom()

def draw(screen: pygame.Surface):
  screen.fill("black")

  current_room.draw(screen)

  for item in current_room.items:
    item.draw(screen)

  for enemy in current_room.enemies:
    enemy.draw(screen)

  for player in current_room.players:
    player.draw(screen)
  
  pygame.display.update()

def update(keys_just_pressed):
  clock.tick(60)
  dt = clock.get_time()
  keys_pressed = pygame.key.get_pressed()

  for enemy in current_room.enemies:
    enemy.update(dt, current_room.players)

  for player in current_room.players:
    player.update(
      dt,
      keys_pressed,
      keys_just_pressed,
      current_room,
    )

while True:
  keys_just_pressed = []
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == pygame.KEYDOWN:
      keys_just_pressed = pygame.key.get_pressed()

  update(keys_just_pressed)
  draw(screen)
