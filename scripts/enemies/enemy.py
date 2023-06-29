import pygame, random
from scripts.enemies.enemy_type import EnemyType
from scripts.character import Character
from scripts.entity import Entity
from scripts.items.item import Item
from data.directions import Directions

class Enemy(Character):
  def __init__(self, enemy_type: EnemyType, x: float, y: float, difficulty_multiplier = 1) -> None:
    super().__init__(
      x = x,
      y = y,
      width = enemy_type.width,
      height = enemy_type.height,
      direction = Directions.DOWN,
      health = enemy_type.health,
      speed = enemy_type.speed,
      spritesheet = enemy_type.spritesheet,
      number_of_frames = enemy_type.number_of_frames,
    )
    self.type = enemy_type
    self.difficulty_multiplier = difficulty_multiplier
    self.health *= difficulty_multiplier
    self.attack_timer = self.type.attack_cooldown

  target = None

  def update(self, dt: int, possible_targets: list[Character], walls: list[Entity]):
    super().update(dt)

    x_before_movement, y_before_movement = self.x, self.y

    if self.is_taking_knockback():
      self.take_knockback(dt)
      self.collider.update(
        (self.x, self.y),
        (self.type.width, self.type.height),
      )
      self.reset_animation()

    elif self.attack_timer > 0:
      self.attack_timer -= dt
      self.reset_animation()

    else:
      self.__choose_target(possible_targets)
      self.__move(dt)
      self.run_animation(dt)

      self.collider.update(
        (self.x, self.y),
        (self.type.width, self.type.height),
      )
      for target in possible_targets:
        if self.is_colliding_with(target):
          self.__attack(target)

    # Colisão com as paredes
    for wall in walls:
      if self.is_colliding_with(wall):
        self.x = x_before_movement
        self.y = y_before_movement

  def draw(self, screen: pygame.Surface):
    direction = 0 if (self.direction == Directions.RIGHT) else 1
    screen.blit(
      source = self.type.spritesheet,
      dest = (
        self.x + self.type.sprite_x_offset,
        self.y - self.type.sprite_y_offset,
      ),
      area = (
        self.animation_frame * (self.type.width + self.type.sprite_x_offset),
        direction * (self.type.height + self.type.sprite_y_offset),
        self.type.width + self.type.sprite_x_offset,
        self.type.height + self.type.sprite_y_offset,
      ),
    )

  def drop_items(self, number_of_players: int) -> list[Item]:
    drops = []

    for drop in self.type.drops:
      if random.randint(1, 100) <= drop[1] * number_of_players:
        drops.append(Item(
          item_type = drop[0],
          x = self.x, y = self.y,
        ))

    return drops

  def __move(self, dt: int):
    if not isinstance(self.target, Character): return

    normalizer = self.__movement_normalizer()

    if self.y < self.target.collider.y:
      self.y += self.type.speed / normalizer * dt
    elif self.y > self.target.collider.y:
      self.y -= self.type.speed / normalizer * dt

    if self.x < self.target.collider.x:
      self.direction = Directions.RIGHT
      self.x += self.type.speed / normalizer * dt
    elif self.x > self.target.collider.x:
      self.direction = Directions.LEFT
      self.x -= self.type.speed / normalizer * dt

  def __movement_normalizer(self) -> float:
    if not isinstance(self.target, Character): return 1

    if self.y < self.target.y and self.x > self.target.x:
      return 1.4
    if self.y < self.target.y and self.x < self.target.x:
      return 1.4
    if self.y > self.target.y and self.x > self.target.x:
      return 1.4
    if self.y > self.target.y and self.x < self.target.x:
      return 1.4
  
    return 1

  def __choose_target(self, possible_targets: list[Character]):
    self.target = None
    if len(possible_targets) > 0:
      self.target = possible_targets[0]
      for target in possible_targets[1:]:
        if self.get_distance_to(target) < self.get_distance_to(self.target):
          self.target = target

  def __attack(self, target: Character):
    target.take_damage(
      damage = self.type.damage * self.difficulty_multiplier,
      direction = self.direction,
      knockback_intensity = self.type.knockback_intensity,
    )
    self.attack_timer = self.type.attack_cooldown
