from pygame import Surface
from scripts.player.weapon.weapon import Weapon
from scripts.player.weapon.weapon_type import WeaponType
from scripts.player.weapon.bullet import Bullet
from scripts.enemies.enemy import Enemy
from scripts.items.item import Item
from scripts.entity import Entity
from data.directions import Directions

class RangedWeapon(Weapon):
  def __init__(self, type: WeaponType) -> None:
    super().__init__(type)

    self.bullets = []

  def draw(self, screen: Surface): pass

  def update(self, dt: int, player_attack: int, entities: list[Entity]):
    bullets_to_be_removed = []

    for entity in entities:
      for bullet in self.bullets:
        if bullet.is_colliding_with(entity):
          if type(entity) == Enemy:
            entity.take_damage(
              damage = self.type.damage * player_attack,
              direction = self.direction,
              knockback_intensity = self.type.knockback_intensity,
            )
          if bullet not in bullets_to_be_removed and type(entity) != Item:
            bullets_to_be_removed.append(bullet)

    for bullet in bullets_to_be_removed:
      self.bullets.remove(bullet)

  def start_attack(self, x: float, y: float, direction: Directions, player_width = 32):
    super().start_attack(x, y, direction)

    # Inversão de width e height se estiver olhando para os lados
    width = self.type.hitbox_width if (direction == Directions.UP or direction == Directions.DOWN) else self.type.hitbox_height
    height = self.type.hitbox_height if (direction == Directions.UP or direction == Directions.DOWN) else self.type.hitbox_width

    # Posicionamento da arma
    match direction:
      case Directions.UP: y -= height
      case Directions.LEFT: x -= width

    # Divisão da colisão da largura igualmente para os dois lados
    if direction == Directions.UP or direction == Directions.DOWN:
      x -= width / 2 - player_width
    elif direction == Directions.LEFT or direction == Directions.RIGHT:
      y -= height / 2 - player_width

    self.bullets.append(
      Bullet(
        sprite = self.type.attack_animation,
        direction = direction,
        speed = self.type.bullet_speed,
        x = x, y = y,
        width = width, height = height,
      )
    )
