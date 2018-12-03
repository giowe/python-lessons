from random import randint, choice
import os

DIRECTIONS = "w", "a", "s", "d"

class Game():
  def __init__(self, levels):
    self.levels = []
    for i in range(levels):
      self.levels.append(World(randint(10, 30), randint(5, 10), randint(2, 10)))

    self.current_level_index = 0

  def get_current_level(self):
    if self.get_current_level_index >= len(self.levels):
      return None
    
    return self.levels[self.current_level_index]

  def game_over(self):
    pass

  def win(self):
    self.current_level_index += 1

  def draw(self):
    os.system("clear")
    level = self.get_current_level()
    if level is None:
      print("A WINNER IS YOU")
    else: 
      print("LEVEL {}".format(self.current_level_index + 1))
      print(self.get_current_level())

  def update(self):
    self.get_current_level().update()

class World():
  def __init__(self, w, h, monsters):
    self.w = w
    self.h = h
    self.player = Player(0, 0, self)
    self.gold = Gold(*self._get_random_coords(), self)
    self.entities = [self.player, self.gold]

    while len(self.entities) - 2 < monsters:
      x, y = self._get_random_coords()

      if self.get_entity(x, y) is None:
        self.entities.append(Monster(x, y, self))

  def update(self):
    for e in self.entities:
      e.update()

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

  def move(self, direction=None):
    if direction is None:
      direction = choice(DIRECTIONS)

    future_x = self.x
    future_y = self.y

    if direction == "w":
      if self.y > 0:
        future_y -= 1
    elif direction == "s":
      if self.y < self.world.h-1:
        future_y += 1
    elif direction == "a":
      if self.x > 0:
        future_x -= 1
    elif direction == "d":
      if self.x < self.world.w-1:
        future_x += 1
    else:
      raise Exeption("comando non valido, le direzioni accettate sono 'w' 'a' 's' 'd'")

    e = self.world.get_entity(future_x, future_y)
    if e is None:
      self.x = future_x
      self.y = future_y
    else:
      self.collide(e)

  def collide(self, entity):
    self_class = self.__class__.__name__
    entity_class = entity.__class__.__name__
    
    if self_class == "Player":
      if entity_class == "Monster":
        print("Game over")
      elif entity_class == "Gold":
        print("WIN")
    elif self_class == "Monster":
      if entity_class == "Player":
        print("Game over")

  def update(self):
    return None

  def __str__(self):
    return self.graphic

class Player(Entity):
  def __init__(self, x, y, world):
    super().__init__(x, y, world, "@")

class Monster(Entity):
  def __init__(self, x, y, world):
    #Entity.__init__(self, x, y, "M")
    super().__init__(x, y, world, "#")

  def update(self):
    self.move()

class Gold(Entity):
  def __init__(self, x, y, world):
    super().__init__(x, y, world, "o")

  def update(self):
    if self.graphic == "O":
      self.graphic = "o"
    else:
      self.graphic = "O"

level1 = World(5, 11, 3)

while True:
  while True:
    direction = input("dove vuoi muoverti? (w, a, s, d)")
    if direction == "q":
      exit()

    if direction in DIRECTIONS:
      level1.player.move(direction)
      level1.update()
      break
    else:
      print("direzione non valida")

