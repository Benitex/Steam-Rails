from typing import Callable
from pygame import Surface

class ItemType:
  def __init__(self, image: Surface, effect: Callable) -> None:
    self.effect = effect
    self.image = image
