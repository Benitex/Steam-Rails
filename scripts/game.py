import pygame
from scripts.map.rooms.initial_room import InitialRoom

class Game: # TODO substituir pelo nome do jogo
  current_room = InitialRoom()
  clock = pygame.time.Clock()

  def draw(self, screen: pygame.Surface):
    screen.fill("black")

    self.current_room.draw(screen)

    for item in self.current_room.items:
      item.draw(screen)

    for enemy in self.current_room.enemies:
      enemy.draw(screen)

    for player in self.current_room.players:
      player.draw(screen)
    
    pygame.display.update()

  def update(self, keys_just_pressed):
    self.clock.tick(60)
    dt = self.clock.get_time()
    keys_pressed = pygame.key.get_pressed()

    for enemy in self.current_room.enemies:
      enemy.update(dt, self.current_room.players)

    for player in self.current_room.players:
      player.update(
        dt,
        keys_pressed,
        keys_just_pressed,
        self.current_room,
      )
