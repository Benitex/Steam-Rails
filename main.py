from sys import exit
import pygame

pygame.init()
screen = pygame.display.set_mode((832 * 2, 480 * 2))

from scripts.game import SteamRails

game = SteamRails()
clock = pygame.time.Clock()
font = pygame.font.Font("graphics/font/circulating_font.ttf", 12 * 2)
music = pygame.mixer.music.load("audio/music/Daily Work.ogg")

pygame.mixer.music.play(loops = -1)
pygame.display.set_caption("Steam Rails")
pygame.display.set_icon(pygame.image.load("graphics/icons/game_icon.jpg"))

while True:
  keys_just_pressed = pygame.key.ScancodeWrapper()
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      keys_just_pressed = pygame.key.get_pressed()
    if event.type == pygame.QUIT or (len(keys_just_pressed) > 0 and keys_just_pressed[pygame.K_ESCAPE]):
      pygame.quit()
      exit()

  clock.tick(60)
  dt = clock.get_time()

  game.update(dt, keys_just_pressed)
  game.draw(screen, font)
