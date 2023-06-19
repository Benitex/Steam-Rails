import pygame
from entity import Entity
from player.player_controls import PlayerControls
from items.item import Item

class Player(Entity):
  def __init__(self, controls: PlayerControls, spritesheet: pygame.Surface, x: float, y: float, items = []) -> None:
    super().__init__(
      x = x,
      y = y,
      width = 32,
      height = 32,
    )
    self.controls = controls
    self.spritesheet = spritesheet

    self.items = items

  items = []
  max_health = 5
  health = 5
  invincible = False
  speed = 0.15

  dodge_speed = 0.3
  dodge_duration = 200
  dodge_timer = dodge_duration

  def is_dead(self) -> bool: return self.health <= 0

  def update(self, dt: int, keys_pressed, keys_just_pressed, room):
    if self.dodge_timer < self.dodge_duration:
      self.__dodge(keys_pressed, dt)
      self.dodge_timer += dt

    elif len(keys_just_pressed) > 0:
      if keys_just_pressed[self.controls.DODGE]:
        self.dodge_timer = 0
      elif keys_just_pressed[self.controls.ATTACK]:
        self.__attack()

    else:
      self.__move(dt, keys_pressed)

    self.collider = pygame.Rect(
      (self.x, self.y + self.height),
      (self.width, self.height),
    )
    self.__collide(keys_just_pressed, room)

  def draw(self, screen: pygame.Surface):
    screen.blit(
      self.spritesheet,
      dest = (self.x, self.y),
      # area = (), TODO adicionar animações
    )

  def __collide(self, keys_just_pressed, room):
    for entity in room.get_entities():
      if self.is_colliding_with(entity):
        if type(entity) == Item:
          if len(keys_just_pressed) > 0 and keys_just_pressed[self.controls.ACTION]:
            self.pick_item(entity)
            room.items.remove(entity)

  def __move(self, dt: int, keys_pressed):
    normalizer = self.__movement_normalizer(keys_pressed)

    if keys_pressed[self.controls.UP]:
      self.y -= self.speed / normalizer * dt
    elif keys_pressed[self.controls.DOWN]:
      self.y += self.speed / normalizer * dt

    if keys_pressed[self.controls.RIGHT]:
      self.x += self.speed / normalizer * dt
    elif keys_pressed[self.controls.LEFT]:
      self.x -= self.speed / normalizer * dt

  def __movement_normalizer(self, keys_pressed) -> float:
    if keys_pressed[self.controls.UP] and keys_pressed[self.controls.RIGHT]:
      return 1.4
    if keys_pressed[self.controls.UP] and keys_pressed[self.controls.LEFT]:
      return 1.4
    if keys_pressed[self.controls.DOWN] and keys_pressed[self.controls.LEFT]:
      return 1.4
    if keys_pressed[self.controls.DOWN] and keys_pressed[self.controls.RIGHT]:
      return 1.4
  
    return 1

  def __attack(self):
    pass # TODO implementar método

  def __dodge(self, keys_pressed, dt):
    self.invincible = True
    normalizer = self.__movement_normalizer(keys_pressed)

    if keys_pressed[self.controls.UP]:
      self.y -= self.dodge_speed / normalizer * dt
    elif keys_pressed[self.controls.DOWN]:
      self.y += self.dodge_speed / normalizer * dt

    if keys_pressed[self.controls.RIGHT]:
      self.x += self.dodge_speed / normalizer * dt
    elif keys_pressed[self.controls.LEFT]:
      self.x -= self.dodge_speed / normalizer * dt

  def pick_item(self, item: Item):
    item.apply_effect(self)
    self.items.append(item)
