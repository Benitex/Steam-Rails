from abc import abstractmethod
import pygame
from scripts.entity import Entity
from data.directions import Directions

class Character(Entity):
  def __init__(self, x: float, y: float, width: int, height: int, direction: Directions, health: int, speed: float, spritesheet: pygame.Surface, number_of_frames: int) -> None:
    super().__init__(x, y, width, height)

    self.direction = direction
    self.health = health
    self.speed = speed

    self.spritesheet = spritesheet
    self.number_of_frames = number_of_frames
    self.frame_duration = 1000 // number_of_frames

  iframes = 400
  iframes_timer = iframes

  knockback_duration = 100
  knockback_timer = knockback_duration
  knockback_direction = None
  knockback_intensity = 0

  animation_frame = 0
  animation_timer = 0

  def is_dead(self) -> bool: return self.health <= 0

  def is_invincible(self) -> bool:
    return self.iframes_timer < self.iframes

  def is_taking_knockback(self) -> bool:
    return self.knockback_timer < self.knockback_duration

  def update(self, dt: int):
    if self.iframes_timer < self.iframes:
      self.iframes_timer += dt

  @abstractmethod
  def draw(self, screen: pygame.Surface): pass

  def draw_collider(self, screen: pygame.Surface):
    if self.is_invincible():
      pygame.draw.rect(screen, "green", self.collider)
    else:
      pygame.draw.rect(screen, "red", self.collider)

  def run_animation(self, dt: int):
    self.animation_timer += dt

    if self.animation_timer > self.frame_duration:
      self.animation_timer = 0
      self.animation_frame += 1
      if self.animation_frame >= self.number_of_frames:
        self.animation_frame = 0

  def reset_animation(self):
    self.animation_frame = 0
    self.animation_timer = 0

  def take_damage(self, damage: int, direction: Directions, knockback_intensity: float):
    if self.is_invincible(): return

    self.health -= damage
    self.iframes_timer = 0
    self.knockback_timer = 0
    self.knockback_direction = direction
    self.knockback_intensity = knockback_intensity

  def take_knockback(self, dt: int):
    self.knockback_timer += dt

    if type(self.knockback_direction) != Directions or self.knockback_intensity <= 0:
      return

    if self.knockback_direction == Directions.DOWN:
      self.y += self.knockback_intensity * dt
    elif self.knockback_direction == Directions.LEFT:
      self.x -= self.knockback_intensity * dt
    elif self.knockback_direction == Directions.RIGHT:
      self.x += self.knockback_intensity * dt
    elif self.knockback_direction == Directions.UP:
      self.y -= self.knockback_intensity * dt
