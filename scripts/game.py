import pygame
from random import randint
from scripts.map.rooms.room import Room
from scripts.map.rooms.initial_room import InitialRoom

class Game: # TODO substituir pelo nome do jogo
  current_room = InitialRoom()
  players = []

  def draw(self, screen: pygame.Surface):
    screen.fill("black")

    self.current_room.draw(screen)

    for item in self.current_room.items:
      item.draw(screen)

    for enemy in self.current_room.enemies:
      enemy.draw(screen)

    for player in self.players:
      player.draw(screen)

    pygame.display.update()

  def update(self, dt: int, keys_just_pressed):
    keys_pressed = pygame.key.get_pressed()

    for enemy in self.current_room.enemies:
      enemy.update(dt, self.players)

    for player in self.players:
      player.update(
        dt,
        keys_pressed,
        keys_just_pressed,
        self.current_room,
      )

    if type(self.current_room) == InitialRoom:
      self.current_room.update(self.players, keys_pressed)
    elif type(self.current_room) == Room:
      self.current_room.update()

    if self.current_room.door.should_change_room(self.players):
      self.move_to_next_room()

  def move_to_next_room(self):
    for player_number, player in enumerate(self.players):
      player.x = 128
      player.y = 128 + player_number * 32

    self.current_room = Room(
      tile_layers_files = [
        open("placeholder/data/initial_room/initial_room_1.csv"),
        open("placeholder/data/initial_room/initial_room_2.csv"),
      ],
      number_of_players = len(self.players),
      number_of_enemies = randint(2, 4),
    )
