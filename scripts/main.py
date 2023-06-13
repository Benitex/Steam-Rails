import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

def draw(screen: pygame.Surface):
  pass

def update():
  clock.tick(60)
  dt = clock.get_time()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  update()
  draw(screen)
