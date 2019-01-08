from random import randint, choice
import os

DIRECTIONS = "w", "a", "s", "d"

class Game():
  def __init__(self, starting_level_index = 0, levels = 2):
    self.game_over_flag = False
    self.win_flag = False

    self.levels = []
    for level_index in range(levels):
      self.levels.append(World(level_index+1, self))

    self.current_level_index = starting_level_index

  def get_current_level(self):
    return self.levels[self.current_level_index]

  def get_player(self):
    return self.get_current_level().player

  def is_game_running(self):
    return self.game_over_flag == False and self.win_flag == False

  def game_over(self):
    self.game_over_flag = True

  def win(self):
    if self.current_level_index >= len(self.levels) -1:
      self.win_flag = True
    else:
      self.current_level_index += 1

  def draw(self):
    os.system("clear")
    level = self.get_current_level()  
    print("---------------------------------------------")
    print("LEVEL {}".format(self.current_level_index + 1))
    print("---------------------------------------------")
    print(level)

    if self.game_over_flag:
      print("LOOOOSER")
    elif self.win_flag:
      print("A WINNER IS YOU")


  def update(self):
    if self.is_game_running():
      self.get_current_level().update()

class World():
  def __init__(self, level_name, game):
    self.game = game
    self.entities = []
    self.player = None
    self.gold = None 
    
    f = open("./levels/{}.br1".format(level_name))
    rows = f.readlines()
    f.close()

    self.h = len(rows)
    self.w = len(rows[0])-1

    for y in range(len(rows)):
      r = rows[y].replace("\n", "")
      for x in range(len(r)):
        char = r[x]
        if char == "#":
          self.entities.append(Wall(x, y, self))
        elif char == "@":
          if self.player is None:
            self.player = Player(x, y, self)
            self.entities.append(self.player)
          else:
            raise Exception("Il player è già presente nel livello")
        elif char == ">":
          self.entities.append(Monster(x, y, self))
        elif char == "o":
          if self.gold is None:
            self.gold = Gold(x, y, self)
            self.entities.append(self.gold)
          else:
            raise Exception("Il gold è già presente nel livello")

    if self.player is None:
      raise Exception("Nel livello manca il player")

    if self.gold is None:
      raise Exception("Nel livello manca il gold")

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
      raise Exception("comando non valido, le direzioni accettate sono 'w' 'a' 's' 'd'")

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
        self.world.game.game_over()
      elif entity_class == "Gold":
        self.world.game.win()
    elif self_class == "Monster":
      if entity_class == "Player":
        self.world.game.game_over()
  
  def update(self):
    return None

  def __str__(self):
    return self.graphic

class Player(Entity):
  def __init__(self, x, y, world):
    super().__init__(x, y, world, "@")

class Wall(Entity):
  def __init__(self, x, y, world):
    super().__init__(x, y, world, "#")

class Monster(Entity):
  def __init__(self, x, y, world):
    #Entity.__init__(self, x, y, "M")
    super().__init__(x, y, world, ">")

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


game = Game(1)

while True:
  while True:
    game.draw()

    if game.is_game_running():
      print("dove vuoi muoverti? (w, a, s, d)")
    
    print("q per uscire")
    command = input()
    
    if command == "q":
      exit()

    if game.is_game_running():
      if command in DIRECTIONS:
        game.get_player().move(command)
        game.update()
        break
      else:
        print("direzione non valida")
