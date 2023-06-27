import pygame
from sys import exit
from scripts.game import Game

pygame.init()
game = Game()
screen = pygame.display.set_mode((608, 384))
clock = pygame.time.Clock()
font = pygame.font.Font("placeholder/graphics/font.ttf", 12) # TODO adicionar fonte real

while True:
  keys_just_pressed = pygame.key.ScancodeWrapper()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if event.type == pygame.KEYDOWN:
      keys_just_pressed = pygame.key.get_pressed()

  clock.tick(60)
  dt = clock.get_time()

  game.update(dt, keys_just_pressed)
  game.draw(screen, font)
