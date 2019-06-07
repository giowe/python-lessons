import os

class Entity:
  def __init__(self, x, y, graphic, level):
    self.x = x
    self.y = y
    self.graphic = graphic
    self.level = level

  def move(self, direction):
    level = self.level
    x = self.x
    y = self.y

    if direction == "up" and y > 0 and level.get_entity_at_coords(x, y - 1) == None:
      self.y -= 1
    elif direction == "down" and y < level.h -1 and level.get_entity_at_coords(x, y + 1) == None:
      self.y += 1
    elif direction == "left" and x > 0 and level.get_entity_at_coords(x -1, y) == None:
      self.x -= 1
    elif direction == "right" and x < level.w -1 and level.get_entity_at_coords(x +1, y) == None:
      self.x += 1

class Player(Entity):
  pass

class Enemy(Entity):
  pass

class Gold(Entity):
  pass

class Obstacle(Entity):
  pass

class Level:
  def __init__(self, w, h, n):
    self.w = w
    self.h = h
    
    self.player = Entity(3, 3, "P", self)
    self.entities = [self.player]
    for i in range(n):
      self.entities.append(Entity(i, 0, "@", self))

  def get_entity_at_coords(self, x, y):
    for e in self.entities:
      if e.x == x and e.y == y:
        return e

  def draw(self):
    os.system("cls")
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if e.x == x and e.y == y:
            print("[{}]".format(e.graphic), end = "") 
            break 
        else:
          print("[ ]", end = "")

      print()


levels = [
  Level(10, 10, 5),
  Level(10, 5, 10)
]

current_level = 0
while True:
  l = levels[current_level]
  l.draw()

  action = input("cosa vuoi fare? ").lower()

  if action == "quit":
    quit()
  elif action == "w":
    l.player.move("up")
  elif action == "a":
    l.player.move("left")
  elif action == "s":
    l.player.move("down")
  elif action == "d":
    l.player.move("right")
  elif action == "+":
    current_level += 1
  elif action == "-":
    current_level -= 1