from typing import Callable
from pygame import Surface, transform

class ItemType:
  def __init__(self, image: Surface, effect: Callable, scale = 2) -> None:
    self.effect = effect
    self.image = transform.scale_by(image, scale).convert_alpha()
