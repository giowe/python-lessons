class World():
  def __init__(self, w, h):
    self.w = w
    self.h = h
    self.entities = []

  def __str__(self):
    out=""
    entities2Draw = self.entities[:]
    for row in range(self.h):
      for col in range(self.w):
        for e in entities2Draw:
          if e.x == col and e.y == row:
            out+="[{}]".format(e.graphic)
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
    return "<Entity {} (x = {}; y = {})>".format(self.graphic, self.x, self.y)

class Player(Entity):
  pass

class Monster(Entity):
  pass

class Gold(Entity):
  pass


level1 = World(5, 10)
e = Entity(2, 5, "X")
level1.entities.append(e)
print(level1)
