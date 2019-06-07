from random import choice, randint
import os
from colorama import Fore, Style

DIRECTIONS = ("up", "down", "left", "right")

class Entity:
  def __init__(self, x, y, graphic, color, level):
    self.x = x
    self.y = y
    self.level = level
    self.graphic = graphic
    self.color = color

  def update(self):
    pass

  def collide(self, entity):
    return False

  def move(self, direction):
    next_x = self.x
    next_y = self.y

    if direction == "up":
      if self.y > 0:
        next_y -= 1
      else:
        next_y = self.level.h - 1
    elif direction == "down":
      if self.y < self.level.h - 1:
        next_y += 1
      else:
        next_y = 0
    elif direction == "left":
      if self.x > 0:
        next_x -= 1
      else:
        next_x = self.level.w - 1
    elif direction == "right":
      if self.x < self.level.w - 1:
        next_x += 1
      else:
        next_x = 0

    e = self.level.get_entity_at_coords(next_x, next_y)
    if e == None or self.collide(e) == True:
      self.x = next_x
      self.y = next_y


class Player(Entity):
  def __init__(self, x, y, level):

    super().__init__(x, y, "@".format(), Fore.GREEN, level)

  def collide(self, entity):
    if isinstance(entity, Collectible):
      self.level.entities.remove(entity)
      self.level.score += 1

      if self.level.score == self.level.max_score:
        self.level.won = True

      return True

    elif isinstance(entity, Enemy):
      self.level.entities.remove(entity)
      self.level.kills += 1
      return False



class Enemy(Entity):
  def __init__(self, x, y, level):
    super().__init__(x, y, "x", Fore.RED, level)

  def collide(self, entity):
    if isinstance(entity, Collectible):
      return True
    elif isinstance(entity, Player):
      self.level.entities.remove(entity)
      self.level.game_over = True
      return True


  def update(self):
    self.move(choice(DIRECTIONS)) 


class Obstacle(Entity):
  def __init__(self, x, y, level):
    super().__init__(x, y, "#", Fore.CYAN, level)


class Collectible(Entity):
  def __init__(self, x, y, level):
    super().__init__(x, y, "*", Fore.YELLOW, level)


class Level:
  def __init__(self, w, h, number_of_monsters, number_of_collectibles, number_of_obstacles, player_x = 0, player_y = 0):
    self.w = w
    self.h = h
    self.player = player = Player(player_x, player_y, self)
    self.entities = [player]
    self.score = 0
    self.kills = 0
    self.max_score = number_of_collectibles
    self.won = False
    self.game_over = False

    count = 0
    while number_of_monsters >= count:
      x = randint(0, self.w - 1)
      y = randint(0, self.h - 1)
      if self.get_entity_at_coords(x, y) == None:
        self.entities.append(Enemy(x, y, self))
        count += 1

    count = 0
    while number_of_collectibles >= count:
      x = randint(0, self.w - 1)
      y = randint(0, self.h - 1)
      if self.get_entity_at_coords(x, y) == None:
        self.entities.append(Collectible(x, y, self))
        count += 1
    
    count = 0
    while number_of_obstacles >= count:
      x = randint(0, self.w - 1)
      y = randint(0, self.h - 1)
      if self.get_entity_at_coords(x, y) == None:
        self.entities.append(Obstacle(x, y, self))
        count += 1

  def get_entity_at_coords(self, x, y):
    for e in self.entities:
      if e.x == x and e.y == y:
        return e

  def update(self):
    for e in self.entities:
      e.update()

  def draw(self):
    os.system("cls")
    print("SCORE: {}".format(self.score))
    print("KILLS: {}".format(self.kills))
    for y in range(self.h):
      for x in range(self.w):
        e = self.get_entity_at_coords(x, y)
        if e != None:
          print("[{}{}{}]".format(e.color, e.graphic, Style.RESET_ALL), end = "")  
        else:
          print("[ ]", end = "")

      print()


levels = [
  Level(3, 3, 1, 1, 1, 1, 1),
  Level(5, 5, 3, 2, 5, 3, 3),
  Level(10, 10, 6, 3, 20, 5, 5),
]

current_level_index = 0 

while True:
  current_level = levels[current_level_index]
 
  current_level.draw()

  if current_level.won:
    current_level_index += 1
    if current_level_index == len(levels):
      print("hai vinto!")
      quit()
    else:
      current_level = levels[current_level_index]

  if current_level.game_over:
    print("LOOOOOOOOOOOOOOOOOSER!")
    quit()

  player = current_level.player

  action = input("che mossa vuoi fare? (w a s d per muoverti, q per uscire)").lower()

  if action == "q":
    quit()
  elif action == "w":
    player.move("up")
  elif action == "a":
    player.move("left")
  elif action == "s":
    player.move("down")
  elif action == "d":
    player.move("right")
  elif action == "+":
    current_level_index += 1
  elif action == "-":
    current_level_index -= 1

  current_level.update()