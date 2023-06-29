import pygame
from scripts.character import Character
from scripts.player.player_controls import PlayerControls
from scripts.player.weapon.weapon import Weapon
from scripts.player.weapon.melee_weapon import MeleeWeapon
from scripts.player.weapon.ranged_weapon import RangedWeapon
from scripts.entity import Entity
from scripts.enemies.enemy import Enemy
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
      health = self.max_health,
      speed = 0.15,
      spritesheet = spritesheet,
      number_of_frames = 11,
    )
    self.controls = controls

    self.items = items or []

  max_health = 5
  attack = 1
  weapon = None

  DODGE_SPEED_MULTIPLIER = 2
  dodge_duration = 300
  dodge_timer = dodge_duration
  attack_timer = 0

  def is_invincible(self) -> bool:
    return self.is_dodging() or self.iframes_timer < self.iframes

  def is_attacking(self) -> bool:
    if not isinstance(self.weapon, Weapon): return False
    return self.attack_timer < self.weapon.type.attack_duration

  def is_dodging(self) -> bool:
    return self.dodge_timer < self.dodge_duration

  # Equipa uma nova arma e retorna a antiga (se houver uma)
  def change_weapon(self, new_weapon: Weapon):
    old_weapon = self.weapon
    self.weapon = new_weapon
    self.attack_timer = new_weapon.type.attack_duration
    if isinstance(self.weapon, Weapon): return old_weapon

  def pick_item(self, item: Item):
    item.apply_effect(self)
    self.items.append(item)

  def take_damage(self, damage: int, direction: Directions, knockback_intensity: float):
    if self.is_invincible(): return

    super().take_damage(damage, direction, knockback_intensity)

  def update(self, dt: int, keys_pressed: pygame.key.ScancodeWrapper, keys_just_pressed: pygame.key.ScancodeWrapper, entities: list[Entity]):
    super().update(dt)

    x_before_movement, y_before_movement = self.x, self.y
    if type(self.weapon) == RangedWeapon:
      for bullet in self.weapon.bullets:
        bullet.update(dt)
      self.weapon.update(self.attack, entities)

    if self.is_taking_knockback():
      self.take_knockback(dt)
      self.reset_animation()

    elif self.is_attacking():
      self.__attack(dt, entities)
      self.reset_animation()

    elif self.is_dodging():
      self.__dodge(keys_pressed, dt)
      self.run_animation(dt)

    elif len(keys_just_pressed) > 0:
      if keys_just_pressed[self.controls.DODGE]:
        self.dodge_timer = 0
      elif keys_just_pressed[self.controls.ATTACK] and isinstance(self.weapon, Weapon):
        self.attack_timer = 0

        x, y = self.collider.x, self.collider.y
        match self.direction:
          case Directions.DOWN: y += self.height
          case Directions.RIGHT: x += self.width

        self.weapon.start_attack(x, y, self.direction)
        self.__attack(dt, entities)
        self.reset_animation()

    elif keys_pressed[self.controls.UP] or keys_pressed[self.controls.DOWN] or keys_pressed[self.controls.LEFT] or keys_pressed[self.controls.RIGHT]:
      self.__move(dt, keys_pressed)
      self.run_animation(dt)

    else:
      self.reset_animation()

    self.collider.update(
      (self.x, self.y),
      (self.width, self.height),
    )
    self.__collide(entities, keys_just_pressed, x_before_movement, y_before_movement)

  def draw(self, screen: pygame.Surface):
    direction = 0
    match self.direction:
      case Directions.DOWN: direction = 0
      case Directions.RIGHT: direction = 1
      case Directions.LEFT: direction = 2
      case Directions.UP: direction = 3

    screen.blit(
      source = self.spritesheet,
      dest = (self.x, self.y - 32),
      area = (
        self.animation_frame * 32,
        direction * 64,
        32,
        64,
      ),
    )

    # Arma
    if type(self.weapon) == MeleeWeapon and self.is_attacking():
      self.weapon.draw(screen)
    elif type(self.weapon) == RangedWeapon:
      for bullet in self.weapon.bullets:
        bullet.draw(screen)

  def __collide(self, entities: list[Entity], keys_just_pressed: pygame.key.ScancodeWrapper, x_before_movement: float, y_before_movement: float):
    for entity in entities:
      if self.is_colliding_with(entity):
        if type(entity) == Item:
          if len(keys_just_pressed) > 0 and keys_just_pressed[self.controls.ACTION]:
            self.pick_item(entity)
            entity.is_picked_up = True

        elif type(entity) == Chest:
            if entity.is_open and len(keys_just_pressed) > 0 and keys_just_pressed[self.controls.ACTION]:
              self.change_weapon(entity.change_weapons(self.weapon))

        elif type(entity) != Enemy: # entities que "empurram" o jogador
          self.x = x_before_movement
          self.y = y_before_movement

  def __move(self, dt: int, keys_pressed: pygame.key.ScancodeWrapper):
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

  def __movement_normalizer(self, keys_pressed: pygame.key.ScancodeWrapper) -> float:
    if keys_pressed[self.controls.UP] and keys_pressed[self.controls.RIGHT]:
      return 1.4
    if keys_pressed[self.controls.UP] and keys_pressed[self.controls.LEFT]:
      return 1.4
    if keys_pressed[self.controls.DOWN] and keys_pressed[self.controls.LEFT]:
      return 1.4
    if keys_pressed[self.controls.DOWN] and keys_pressed[self.controls.RIGHT]:
      return 1.4
  
    return 1

  def __dodge(self, keys_pressed: pygame.key.ScancodeWrapper, dt: int):
    self.dodge_timer += dt
    normalizer = self.__movement_normalizer(keys_pressed)

    if keys_pressed[self.controls.UP]:
      self.y -= self.speed * self.DODGE_SPEED_MULTIPLIER / normalizer * dt
    elif keys_pressed[self.controls.DOWN]:
      self.y += self.speed * self.DODGE_SPEED_MULTIPLIER / normalizer * dt

    if keys_pressed[self.controls.RIGHT]:
      self.x += self.speed * self.DODGE_SPEED_MULTIPLIER / normalizer * dt
    elif keys_pressed[self.controls.LEFT]:
      self.x -= self.speed * self.DODGE_SPEED_MULTIPLIER / normalizer * dt

  def __attack(self, dt: int, entities: list):
    if not isinstance(self.weapon, Weapon):
      raise Exception("No weapon equiped in instance of Player")

    self.attack_timer += dt
    if type(self.weapon) == MeleeWeapon:
      self.weapon.update(
        player_attack = self.attack,
        entities = entities,
      )
