import pygame
from scripts.character import Character
from scripts.player.player_controls import PlayerControls
from scripts.player.weapon.weapon import Weapon
from scripts.items.item import Item
from scripts.map.objects.chest import Chest
from data.directions import Directions

class Player(Character):
  def __init__(self, controls: PlayerControls, spritesheet: pygame.Surface, x: float, y: float, items = None) -> None:
    super().__init__(
      x = x,
      y = y,
      width = 32,
      height = 32,
      direction = Directions.UP,
      spritesheet = spritesheet,
      health = self.max_health,
      speed = 0.15,
    )
    self.controls = controls

    self.items = items or []

  max_health = 5
  iframes = 300
  weapon = None

  dodge_speed = 0.3
  dodge_duration = 200
  dodge_timer = dodge_duration
  attack_timer = 0
  iframes_timer = iframes

  def is_invincible(self) -> bool:
    return self.is_dodging() or self.iframes_timer < self.iframes

  def is_attacking(self) -> bool:
    if type(self.weapon) != Weapon: return False
    return self.attack_timer < self.weapon.type.attack_duration

  def is_dodging(self) -> bool:
    return self.dodge_timer < self.dodge_duration

  # Equipa uma nova arma e retorna a antiga (se houver uma)
  def change_weapon(self, new_weapon: Weapon):
    old_weapon = self.weapon
    self.weapon = new_weapon
    self.attack_timer = new_weapon.type.attack_duration
    if type(old_weapon) == Weapon: return old_weapon

  def pick_item(self, item: Item):
    item.apply_effect(self)
    self.items.append(item)

  def take_damage(self, damage: int, direction: Directions, knockback_intensity: float):
    if self.is_invincible(): return

    super().take_damage(damage, direction, knockback_intensity)
    self.iframes_timer = 0

  def update(self, dt: int, keys_pressed, keys_just_pressed, room):
    if self.iframes_timer < self.iframes:
      self.iframes_timer += dt

    if self.is_taking_knockback():
      self.take_knockback(dt)

    elif self.is_attacking():
      self.__attack(dt = dt, enemies = room.enemies)

    elif self.is_dodging():
      self.__dodge(keys_pressed, dt)

    elif len(keys_just_pressed) > 0:
      if keys_just_pressed[self.controls.DODGE]:
        self.dodge_timer = 0
      elif keys_just_pressed[self.controls.ATTACK]:
        if type(self.weapon) == Weapon:
          self.attack_timer = 0
          self.__attack(dt = dt, enemies = room.enemies)
        # else: TODO avisar que nenhuma arma está equipada

    else:
      self.__move(dt, keys_pressed)

    self.collider = pygame.Rect(
      (self.x, self.y + 32),
      (self.width, self.height),
    )
    self.__collide(keys_just_pressed, room)

  def draw(self, screen: pygame.Surface):
    screen.blit(
      self.spritesheet,
      dest = (self.x, self.y),
      # area = (), TODO adicionar animações
    )
    if type(self.weapon) == Weapon and self.is_attacking():
      self.weapon.draw(screen)

  def __collide(self, keys_just_pressed, room):
    for entity in room.get_entities():
      if self.is_colliding_with(entity):
        if type(entity) == Item:
          if len(keys_just_pressed) > 0 and keys_just_pressed[self.controls.ACTION]:
            self.pick_item(entity)
            room.items.remove(entity)

        if type(entity) == Chest:
          if len(keys_just_pressed) > 0 and keys_just_pressed[self.controls.ACTION]:
            self.change_weapon(entity.change_weapons(self.weapon))

  def __move(self, dt: int, keys_pressed):
    normalizer = self.__movement_normalizer(keys_pressed)

    if keys_pressed[self.controls.UP]:
      self.direction = Directions.UP
      self.y -= self.speed / normalizer * dt
    elif keys_pressed[self.controls.DOWN]:
      self.direction = Directions.DOWN
      self.y += self.speed / normalizer * dt

    if keys_pressed[self.controls.RIGHT]:
      self.direction = Directions.RIGHT
      self.x += self.speed / normalizer * dt
    elif keys_pressed[self.controls.LEFT]:
      self.direction = Directions.LEFT
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

  def __dodge(self, keys_pressed, dt):
    self.dodge_timer += dt
    normalizer = self.__movement_normalizer(keys_pressed)

    if keys_pressed[self.controls.UP]:
      self.y -= self.dodge_speed / normalizer * dt
    elif keys_pressed[self.controls.DOWN]:
      self.y += self.dodge_speed / normalizer * dt

    if keys_pressed[self.controls.RIGHT]:
      self.x += self.dodge_speed / normalizer * dt
    elif keys_pressed[self.controls.LEFT]:
      self.x -= self.dodge_speed / normalizer * dt

  def __attack(self, dt: int, enemies: list):
    if type(self.weapon) != Weapon:
      raise Exception("No weapon equiped in instance of Player")

    self.attack_timer += dt
    self.weapon.update(
      enemies = enemies,
      # TODO adicionar posicionamento por direção do jogador
      x = self.x,
      y = self.y,
    )
