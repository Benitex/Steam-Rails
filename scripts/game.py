import pygame
from random import randint
from scripts.map.rooms.room import Room
from scripts.map.rooms.initial_room import InitialRoom
from scripts.player.player import Player
from scripts.enemies.enemy import Enemy
from scripts.player.player_ui_bar import PlayerUIBar

class Game: # TODO substituir pelo nome do jogo
  current_room = InitialRoom()
  room_number = 0
  players = []

  def draw(self, screen: pygame.Surface, font: pygame.font.Font):
    screen.fill("black")

    self.current_room.draw(screen)

    for item in self.current_room.items:
      item.draw(screen)

    for enemy in self.current_room.enemies:
      enemy.draw(screen)

    for player in self.players:
      player.draw(screen)

    # UI
    for player_number, player in enumerate(self.players):
      PlayerUIBar(
        player = player,
        x = 16 + 180 * player_number,
        y = 16,
      ).draw(screen)

    screen.blit(
      source = font.render(f"Room number: {self.room_number}", False, "white"),
      dest = (10, 360),
    )
    if len(self.players) == 0 and type(self.current_room) != InitialRoom:
      screen.blit(
        source = font.render("Press space to restart.", False, "white"),
        dest = (180, 320),
      )

    pygame.display.update()

  def update(self, dt: int, keys_just_pressed):
    if len(self.players) == 0 and len(keys_just_pressed) > 0 and (keys_just_pressed[pygame.K_SPACE] or keys_just_pressed[pygame.K_RETURN]):
      self.current_room = InitialRoom()
      self.room_number = 0

    keys_pressed = pygame.key.get_pressed()

    self.remove_dead(self.players, self.current_room.enemies)

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
      player.x = 96
      player.y = 128 + player_number * 32

    self.current_room = Room(
      tile_layers_files = [
        open("placeholder/data/initial_room/initial_room_1.csv"),
        open("placeholder/data/initial_room/initial_room_2.csv"),
      ],
      number_of_players = len(self.players),
    )
    self.room_number += 1

  def remove_dead(self, players: list[Player], enemies: list[Enemy]):
    dead_players = []
    for player in players:
      if player.is_dead(): dead_players.append(player)
    for dead_player in dead_players:
      players.remove(dead_player)

    dead_enemies = []
    for enemy in enemies:
      if enemy.is_dead():
        dead_enemies.append(enemy)
        self.current_room.items += enemy.drop_items()

    for dead_enemy in dead_enemies:
      enemies.remove(dead_enemy)
