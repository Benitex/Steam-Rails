import pygame
from map.rooms.room import Room
from player.player import Player
from player.player_controls import PlayerControls

class InitialRoom(Room):
  def __init__(self) -> None:
    super().__init__(
      players = [
        Player(
          x = 190, y = 192,
          spritesheet = pygame.image.load("placeholder/graphics/player.png"), # TODO adicionar o sprite real
          controls = PlayerControls(
            up = pygame.K_UP,
            down = pygame.K_DOWN,
            left = pygame.K_LEFT,
            right = pygame.K_RIGHT,
            action = pygame.K_SPACE,
            attack = pygame.K_SPACE,
            dodge = pygame.K_LSHIFT,
          ),
        ),
        Player(
          x = 290, y = 192,
          spritesheet = pygame.image.load("placeholder/graphics/player.png"), # TODO adicionar o sprite real
          controls = PlayerControls(
            up = pygame.K_w,
            down = pygame.K_s,
            left = pygame.K_a,
            right = pygame.K_d,
            action = pygame.K_SPACE,
            attack = pygame.K_SPACE,
            dodge = pygame.K_LSHIFT,
          ),
        ),
      ],
      tile_layers_files = [
        open("placeholder/data/initial_room/initial_room_1.csv"),
        open("placeholder/data/initial_room/initial_room_2.csv"),
      ],
      enemies_amount = 0,
      chests = [
        # TODO adicionar armas aleatórias no baú, uma ranged e uma melee
      ],
    )

  def add_players(self):
    pass # TODO cógido para os jogadores "logarem"
