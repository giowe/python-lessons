from random import randint

class World():
  def __init__(self, w, h, monsters):
    self.w = w
    self.h = h
    self.entities = []

    while len(self.entities) < monsters:
      x, y = self._get_random_coords()
      
      if self.get_entity(x, y) is None:
        self.entities.append(Monster(x, y))

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
  def __init__(self, x, y, graphic):
    self.x = x
    self.y = y
    self.graphic = graphic

  def __str__(self):
    return self.graphic

class Player(Entity):
  def __init__(self, x, y):
    super().__init__(x, y, "@")

class Monster(Entity):
  def __init__(self, x, y):
    # Entity.__init__(self, x, y, "M")
    super().__init__(x, y, "#")

class Gold(Entity):
  def __init__(self, x, y):
    super().__init__(x, y, "*")


level1 = World(5, 10, 3)
print(level1)