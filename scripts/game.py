import pygame
from scripts.map.rooms.room import Room
from scripts.map.rooms.initial_room import InitialRoom
from scripts.player.player import Player
from scripts.enemies.enemy import Enemy
from scripts.items.item import Item
from scripts.player.player_ui_bar import PlayerUIBar

class SteamRails:
  current_room = InitialRoom()
  room_number = 0
  players = []

  DOOR_SOUND_EFFECT = pygame.mixer.Sound("audio/sound_effects/door.mp3")

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
        x = 16 + 288 * player_number,
        y = 16,
      ).draw(screen, font)

    screen.blit(
      source = font.render(f"Room number: {self.room_number}", False, "white"),
      dest = (32 * 2, 448 * 2),
    )
    if len(self.players) == 0 and type(self.current_room) != InitialRoom:
      screen.blit(
        source = font.render("Press space to restart.", False, "white"),
        dest = (288 * 2, 320 * 2),
      )

    pygame.display.update()

  def update(self, dt: int, keys_just_pressed: pygame.key.ScancodeWrapper):
    if len(self.players) == 0 and len(keys_just_pressed) > 0 and (keys_just_pressed[pygame.K_SPACE] or keys_just_pressed[pygame.K_RETURN]):
      self.current_room = InitialRoom()
      self.room_number = 0

    keys_pressed = pygame.key.get_pressed()

    self.remove_dead(self.players, self.current_room.enemies, self.current_room.items)

    for enemy in self.current_room.enemies:
      enemy.update(dt, self.players, self.current_room.walls)

    for player in self.players:
      player.update(
        dt = dt,
        keys_pressed = keys_pressed,
        keys_just_pressed = keys_just_pressed,
        entities = self.current_room.get_entities(),
      )

    if type(self.current_room) == InitialRoom:
      self.current_room.update(self.players, keys_pressed)
    elif type(self.current_room) == Room:
      self.current_room.update()

    if self.current_room.door.should_change_room(self.players):
      self.move_to_next_room()

  def move_to_next_room(self):
    pygame.mixer.Sound.play(self.DOOR_SOUND_EFFECT)

    for player_number, player in enumerate(self.players):
      player.x = 160 * 2
      player.y = (224 + player_number * 32) * 2

      # Desativando ataques
      player.attack_timer = player.weapon.type.attack_duration

      bullets_to_be_removed = []
      if not player.weapon.type.is_melee:
        for bullet in player.weapon.bullets:
          bullets_to_be_removed.append(bullet)
      for bullet in bullets_to_be_removed:
        player.weapon.bullets.remove(bullet)

    self.current_room = Room(
      tile_layers_files = [
        open("data/room/room_1.csv"),
        open("data/room/room_2.csv"),
        open("data/room/room_3.csv"),
      ],
      number_of_players = len(self.players),
      enemy_difficulty_multiplier = 1 + self.room_number // 10,
    )
    self.room_number += 1

  def remove_dead(self, players: list[Player], enemies: list[Enemy], items: list[Item]):
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

    picked_up_items = []
    for item in items:
      if item.is_picked_up:
        picked_up_items.append(item)
    for item in picked_up_items:
      items.remove(item)
