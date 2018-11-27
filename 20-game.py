from random import randint, choice
import os

class World():
  def __init__(self, w, h, monsters):
    self.w = w
    self.h = h
    self.entities = []
    self.player = Player(1, 1, self)
    self.entities.append(self.player)

    while len(self.entities) < monsters:
      x, y = self._get_random_coords()
      
      if self.get_entity(x, y) is None:
        self.entities.append(Monster(x, y, self))

  def _get_random_coords(self):
    return (randint(0, self.w -1), randint(0, self.h -1))

  def get_entity(self, x, y):
    for e in self.entities:
      if e.x == x and e.y == y:
        return e

  def __str__(self):
    out=""
    entities2Draw = self.entities[:]
    for row in range(self.h):
      for col in range(self.w):
        for e in entities2Draw:
          if e.x == col and e.y == row:
            out+="[{}]".format(e)
            entities2Draw.remove(e)
            break
        else:
          out+="[ ]"

      out+="\n"
    return out


class Entity():
  def __init__(self, x, y, world, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic
    self.world = world

  def __str__(self):
    return self.graphic

  def move(self, direction=None):
    if direction is None:
      direction = choice(("w", "a", "s", "d"))

    future_x = self.x
    future_y = self.y

    if direction == "w":
      if self.y > 0:
        future_y -= 1
    elif direction == "s":
      if self.y < self.world.h -1:
        future_y += 1
    elif direction == "d":
      if self.x < self.world.w -1:
        future_x += 1
    elif direction == "a":
      if self.x > 0:
        future_x -= 1
    else:
      raise Exception("direction must be 'w' 'a' 's' or 'd'")

    if self.check_collision(future_x, future_y) == False:
      self.x = future_x
      self.y = future_y


  def check_collision(self, x, y):
    e = self.world.get_entity(x, y)
    if e is None:
      return False
    else:
      return True


class Player(Entity):
  def __init__(self, x, y, world):
    super().__init__(x, y, world, "@")

class Monster(Entity):
  def __init__(self, x, y, world):
    #Entity.__init__(self, x, y, "M")
    super().__init__(x, y, world, "M")

class Gold(Entity):
  def __init__(self, x, y, world):
    super().__init__(x, y, world, "*")


level1 = World(5, 10, 3)

while True:
  os.system('clear')
  print(level1)
  direction = input("dove vuoi muoverti? ")
  level1.player.move(direction)