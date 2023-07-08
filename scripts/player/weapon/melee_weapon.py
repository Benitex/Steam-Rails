import pygame
from scripts.player.weapon.weapon import Weapon
from scripts.player.weapon.weapon_type import WeaponType
from scripts.entity import Entity
from scripts.enemies.enemy import Enemy
from data.directions import Directions

class MeleeWeapon(Weapon, Entity):
  def __init__(self, type: WeaponType) -> None:
    Weapon.__init__(self, type)
    Entity.__init__(self, 0, 0, 0, 0)

  animation_frame = 0
  animation_timer = 0

  def draw(self, screen: pygame.Surface):
    width, height = self.__get_directional_dimensions()

    y = 0
    match self.direction:
      case Directions.RIGHT:
        y = self.type.hitbox_height
      case Directions.LEFT:
        y = self.type.hitbox_height + self.type.hitbox_width
      case Directions.UP:
        y = self.type.hitbox_height + self.type.hitbox_width * 2

    screen.blit(
      source = self.type.attack_animation,
      dest = (self.x, self.y),
      area = (
        self.animation_frame * width,
        y,
        width,
        height,
      ),
    )

  def update(self, dt: int, player_attack: int, entities: list[Entity]):
    for enemy in entities:
      if type(enemy) == Enemy and self.is_colliding_with(enemy):
        enemy.take_damage(
          damage = self.type.damage * player_attack,
          direction = self.direction,
          knockback_intensity = self.type.knockback_intensity,
        )
    self.__run_animation(dt)

  def start_attack(self, x: float, y: float, direction: Directions, player_width = 32):
    super().start_attack(x, y, direction)

    width, height = self.__get_directional_dimensions()
    self.animation_frame = 0
    self.animation_timer = 0

    # Posicionamento da arma
    match direction:
      case Directions.UP: self.y -= height
      case Directions.LEFT: self.x -= width

    # Divisão da colisão da largura igualmente para os dois lados
    if direction == Directions.UP or direction == Directions.DOWN:
      self.x -= width / 2 - player_width
    elif direction == Directions.LEFT or direction == Directions.RIGHT:
      self.y -= height / 2 - player_width

    self.collider = pygame.Rect(self.x, self.y, width, height)

  def __run_animation(self, dt: int):
    self.animation_timer += dt

    if self.animation_timer > self.type.attack_duration / self.type.number_of_frames:
      self.animation_timer = 0
      self.animation_frame += 1
      if self.animation_frame >= self.type.number_of_frames:
        self.animation_frame = 0

  # Inversão de width e height se estiver olhando para os lados, retorna as width e height finais
  def __get_directional_dimensions(self) -> tuple[int, int]:
    return (
      self.type.hitbox_width if (self.direction == Directions.UP or self.direction == Directions.DOWN) else self.type.hitbox_height,
      self.type.hitbox_height if (self.direction == Directions.UP or self.direction == Directions.DOWN) else self.type.hitbox_width,
    )
