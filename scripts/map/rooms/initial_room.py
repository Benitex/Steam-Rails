from map.rooms.room import Room
from map.objects.chest import Chest

class InitialRoom(Room):
  def __init__(self) -> None:
    super().__init__(
      tile_layers_files = [
        open("placeholder/data/initial_room/initial_room_1.csv"),
        open("placeholder/data/initial_room/initial_room_2.csv"),
      ],
      chests = [
        # TODO adicionar armas aleatórias no baú, uma ranged e uma melee
      ],
    )
    self.enemies = []
