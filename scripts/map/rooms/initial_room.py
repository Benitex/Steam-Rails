import pygame, random
from scripts.map.rooms.room import Room
from scripts.map.objects.chest import Chest
from scripts.player.player import Player
from scripts.player.player_controls import PlayerControls
from data.weapons import melee_weapons, ranged_weapons

class InitialRoom(Room):
  def __init__(self) -> None:
    super().__init__(
      tile_layers_files = [
        open("placeholder/data/initial_room/initial_room_1.csv"),
        open("placeholder/data/initial_room/initial_room_2.csv"),
      ],
      number_of_players = 0,
      number_of_enemies = 0,
      chests = [
        Chest(
          weapon_type = random.choice(melee_weapons),
          is_infinite = True,
          sprite = self.CHEST_SPRITE,
          x = 224, y = 128,
        ),
        Chest(
          weapon_type = random.choice(ranged_weapons),
          is_infinite = True,
          sprite = self.CHEST_SPRITE,
          x = 352, y = 128,
        ),
      ],
    )

  PLAYER_CONTROLS = [
    PlayerControls(
      up = pygame.K_UP,
      down = pygame.K_DOWN,
      left = pygame.K_LEFT,
      right = pygame.K_RIGHT,
      action = pygame.K_SPACE,
      attack = pygame.K_SPACE,
      dodge = pygame.K_LSHIFT,
    ),
    PlayerControls(
      up = pygame.K_w,
      down = pygame.K_s,
      left = pygame.K_a,
      right = pygame.K_d,
      action = pygame.K_SPACE,
      attack = pygame.K_SPACE,
      dodge = pygame.K_LSHIFT,
    ),
  ]
  PLAYER_SPRITES = [
    # TODO adicionar sprites reais
    pygame.image.load("placeholder/graphics/player.png"),
    pygame.image.load("placeholder/graphics/player.png"),
    pygame.image.load("placeholder/graphics/player.png"),
  ]

  def add_players(self, players: list[Player], keys_pressed):
    number_of_players = len(players)
    if number_of_players > 3: return

    for controls in self.PLAYER_CONTROLS:
      if controls.is_any_key_in_controls_pressed(keys_pressed):
        for player in players:
          if player.controls.is_any_key_in_controls_pressed(keys_pressed):
            return

        players.append(Player(
          x = 192 + number_of_players * 96,
          y = 192,
          controls = controls,
          spritesheet = self.PLAYER_SPRITES[number_of_players],
        ))
