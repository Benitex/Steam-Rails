from scripts.player.player import Player

def modify_max_health(player: Player, percentage: float):
  player.max_health = int(player.max_health * percentage)
  heal(player, percentage - 1)

def heal(player: Player, percentage: float):
  player.health += int(player.max_health * percentage)
  if player.health > player.max_health:
    player.health = player.max_health

def modify_attack(player: Player, amount: int):
  player.attack += amount
  if player.attack < 1: player.attack = 1

def modify_speed(player: Player, percentage: float):
  player.speed *= percentage

def modify_knockback_duration(player: Player, amount: int):
  player.knockback_duration += amount
  if player.knockback_duration < 0: player.knockback_duration = 0
  player.knockback_timer = player.knockback_duration

def modify_dodge_speed_multiplier(player: Player, amount: float):
  player.dodge_speed_multiplier += amount
  if player.dodge_speed_multiplier <= 0: player.dodge_speed_multiplier = 0.1
